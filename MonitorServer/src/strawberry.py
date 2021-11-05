#===============================================================
#
#  Beam profile monitor screen control system
#
#         Original Author: Garam HAHN  <garam.hahn@gmail.com>
#                  Author: Seohyeon AN <klar.wind0425@gmail.com>
#
#===============================================================
#!/usr/bin/env python3
import os, sys
import logging
import threading
import time

import RPi.GPIO as GPIO
from caproto.server import PVGroup, pvproperty, ioc_arg_parser, run

from src.variables import *

class Strawberry(PVGroup):
    request = pvproperty(value=0, doc="Control command")
    low = pvproperty(value=0, doc='Lower limit switch')
    high = pvproperty(value=0, doc='Upper limit switch')
    relay = pvproperty(value=0, doc='Relay switch')
    status = pvproperty(value=0, doc="Actuator status")

    @request.startup
    async def request(self, instance, async_lib):
        self.request_queue = async_lib.ThreadsafeQueue()
        self.status_queue = async_lib.ThreadsafeQueue()

        thread = threading.Thread(target=self.handle_screen,
                                  daemon=True)
        thread.start()

        while True:
            value = await self.status_queue.async_get()
            await self.status.write(value)
            await self.high.write(GPIO.input(UPPER_SWITCH))
            await self.low.write(GPIO.input(LOWER_SWITCH))
            await self.request.write(0)

    @request.putter
    async def request(self, instance, command):
        await self.request_queue.async_put(command)
        return command

    def initialize(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        from src.main import BASE_PATH
        from datetime import datetime
        today = datetime.today()
        file_handler = logging.FileHandler(os.path.join(BASE_PATH, 'log', f"cranberry_{today.strftime('%Y%m%d')}.log"))
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
        GPIO.setup([UPPER_SWITCH, LOWER_SWITCH], GPIO.IN)
        GPIO.setup(RELAY, GPIO.OUT)

        ### For Relay test
        GPIO.setup([12, 16], GPIO.IN)

        self.last_switch = None

    def handle_screen(self):
        while(True):
            command = self.request_queue.get()
            if command == 0: continue
            try:
                self.logger.info(f"Upper: {GPIO.input(UPPER_SWITCH)}, Lower: {GPIO.input(LOWER_SWITCH)}")
                upper_switch_status = GPIO.input(UPPER_SWITCH) + 10
                lower_switch_status = int(GPIO.input(LOWER_SWITCH) + 10)
            except:
                self.logger.exception("Switches are not connected. Please, handle the problem.")
                continue

            if upper_switch_status == SWITCH_OFF and lower_switch_status == SWITCH_OFF:
                if self.last_switch == UPPER_SWITCH:
                    actuator_status = ACTUATOR_GOES_DOWN
                elif self.last_switch == LOWER_SWITCH:
                    actuator_status = ACTUATOR_GOES_UP
                else:
                    actuator_status = ACTUATOR_ERROR
            elif upper_switch_status == SWITCH_OFF and lower_switch_status == SWITCH_ON:
                actuator_status = ACTUATOR_UP
                self.last_switch = UPPER_SWITCH
            elif upper_switch_status == SWITCH_ON and lower_switch_status == SWITCH_OFF:
                actuator_status = ACTUATOR_DOWN
                self.last_switch = LOWER_SWITCH
            else:
                actuator_status = ACTUATOR_ERROR

            if actuator_status == ACTUATOR_ERROR:
                self.logger.exception(f"UpperSwitch: {upper_switch_status}, LowerSwitch: {lower_switch_status}. The actuator cannot catch the position itself. Please, handle the problem.")
                self.status_queue.put(actuator_status)
                continue
        
            try:
                if command == REQUEST_STATUS:
                    if actuator_status == ACTUATOR_UP:
                        self.logger.info("Status: the screen is up.")
                    elif actuator_status == ACTUATOR_DOWN:
                        self.logger.info("Status: the screen is down.")
                    elif actuator_status == ACTUATOR_GOES_DOWN:
                        self.logger.info("Status: the screen goes down.")
                    elif actuator_status == ACTUATOR_GOES_UP:
                        self.logger.info("Status: the screen goes up.")
                elif command == REQUEST_GO_UP:
                    GPIO.output(RELAY, False)
                elif command == REQUEST_GO_DOWN:
                    GPIO.output(RELAY, True)
            except:
                self.logger.exception("Problem handling request.")
            finally:
                self.status_queue.put(actuator_status)
