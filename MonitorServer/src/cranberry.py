#!/usr/bin/env python3
import os, sys
import logging
import threading, queue

from src.variables import *
from caproto.server import PVGroup, pvproperty, SubGroup

DEVMODE = True
if not DEVMODE:
    import RPi.GPIO as GPIO

log_queue = queue.Queue()

class ProfileMonitor(PVGroup):
    REQUEST = pvproperty(value=0, doc='Request order to actuator')
    STATUS = pvproperty(value=0, doc='PV status')

    def __init__(self, *args, num, gpio, **kwargs):
        super().__init__(*args, **kwargs)
        self.connected = False
        self.number = num
        self.gpio = gpio
        self.last_status = None

        if not DEVMODE:
            GPIO.setup([self.gpio['UPPER_SWITCH'], self.gpio['LOWER_SWITCH']], GPIO.IN)
            GPIO.setup(self.gpio['RELAY'], GPIO.OUT)

    @REQUEST.startup
    async def REQUEST(self, instance, async_lib):
        self.request_queue = async_lib.ThreadsafeQueue()
        self.status_queue = async_lib.ThreadsafeQueue()
        thread = threading.Thread(target=self.handle_screen, daemon=True)
        thread.start()

        value = await self.status_queue.async_get()
        await self.STATUS.write(value)
        await self.REQUEST.write(0)
        
    @REQUEST.putter
    async def REQUEST(self, instance, command):
        await self.request_queue.async_put(command)

    def handle_screen(self):
        while True:
            if not self.connected: self.check_connection()
            if self.connected:
                request = self.request_queue.get()
                if request == REQUEST_STATUS:
                    self.update_status(request)
                else:
                    if DEVMODE:
                        continue
                    else:
                        if request == REQUEST_GO_UP:
                            GPIO.output(self.gpio['RELAY'], False)
                        elif request == REQUEST_GO_DOWN:
                            GPIO.output(self.gpio['RELAY'], True)

    def update_status(self, request):
        status = ACTUATOR_ERROR
        if DEVMODE:
            self.status_queue.put(status)
            log_queue.put(f"INFO:Develpment mode - Monitor{self.number} Status is alwasy ACTUATOR_ERROR(-1).")
        else:
            if request == REQUEST_NOTHING: return
            try:
                upper_status = GPIO.input(self.gpio['UPPER_SWITCH'])
                lower_status = GPIO.input(self.gpio['LOWER_SWITCH'])
                log_queue.put(f"INFO:Monitor{self.number} - Upper switch {upper_status}, Lower switch {lower_status}")
            except:
                log_queue.put(f"ERROR:Monitor{self.number} - The status of the limit switch is unknown.")
                return
            
            if upper_status == SWITCH_OFF and lower_status == SWITCH_OFF:
                if self.last_status == ACTUATOR_DOWN:
                    status = ACTUATOR_GOES_UP
                    log_queue.put(f"INFO:Monitor{self.number} - The screen goes up.")
                elif self.last_status == ACTUATOR_UP:
                    status = ACTUATOR_GOES_DOWN
                    log_queue.put(f"INFO:Monitor{self.number} - The screen goes down.")
            elif upper_status == SWITCH_ON and lower_status == SWITCH_OFF:
                status = ACTUATOR_DOWN
                log_queue.put(f"INFO:Monitor{self.number} - The screen up.")
            elif upper_status == SWITCH_OFF and lower_status == SWITCH_ON:
                status = ACTUATOR_UP
                log_queue.put(f"INFO:Monitor{self.number} - The screen down.")

            self.last_status = status
            self.status_queue.put(status)
            if status == ACTUATOR_ERROR:
                log_queue.put(f"ERROR:Monitor{self.number} - The actuator cannot catch the position itself. Please, handle the problem.")

    def check_connection(self):
        if DEVMODE:
            log_queue.put(f"INFO:Development mode - Monitor{self.number} controller is always connected.")
            self.connected= True
        else:
            upper_status = GPIO.input(self.gpio['UPPER_SWITCH'])
            lower_status = GPIO.input(self.gpio['LOWER_SWITCH'])
            if upper_status == lower_status == 0 and not self.connected:
                log_queue.put(f"ERROR:Monitor{self.number} - Any limit switches are not connected or the actuator is somewhere inside the cylinder.")
                self.connected = False
            elif upper_status == lower_status == 1:
                log_queue.put(f"ERROR:Monitor{self.number} - Both switches look activated.")
                self.connected = False
            else:
                log_queue.put(f"STATUS:Monitor{self.number} - BPM is connected.")
                self.connected = True
            
class Cranberry(PVGroup):
    """
    X-ray Scintillator screen beam profile monitor control system
    """
    for i in range(NUMBER_OF_MONITORS):
        locals()[f'{PV_NAME_RANK1}{i}'] = SubGroup(ProfileMonitor, num=i, gpio=GPIO_MAP[f'{PV_NAME_RANK1}{i}'])
    #TERMINATE = pvproperty(value=0, doc='Turn off cranberry.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not DEVMODE: GPIO.setmode(GPIO.BCM)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        from main import BASE_PATH
        from datetime import datetime
        today = datetime.today()
        if not os.path.exists(os.path.join(BASE_PATH, 'log')):
            os.makedirs(os.path.join(BASE_PATH, 'log'))
        file_handler = logging.FileHandler(os.path.join(BASE_PATH, 'log',  f"Cranberry_{today.strftime('%Y%m%d')}.log"))
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        thread = threading.Thread(target=self.receive_log, daemon=True)
        thread.start()

    def receive_log(self):
        while True:
            element = log_queue.get()
            if element is None: return
            else:
                level, message = element.split(":")
                if level == "DEBUG": self.logger.debug(message)
                elif level == "INFO": self.logger.info(message)
                elif level == "WARNING": self.logger.warning(message)
                elif level == "ERROR": self.logger.error(message)
                elif level == "CRITICAL": self.logger.critical(message)



