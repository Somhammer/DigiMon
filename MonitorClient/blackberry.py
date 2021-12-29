import os, sys
import time
import asyncio

from PySide6.QtCore import *
from caproto.threading.client import Context

from variables import *

class Blackberry(QThread):
    for i in range(NUMBER_OF_MONITORS):
        locals()[f'{PV_NAME_RANK1.lower()}{i}_request'] = None
        locals()[f'{PV_NAME_RANK1.lower()}{i}_status'] = None

    status_signal = Signal(str)
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.name = "Profile Monitor Controller"

        self.working = False
        self.connected = False
        self.monitor = None
        self.pvs = {}
        self.context = None
        self.request = None
        self.status = None
        self.previous_request = None
        self.request = None

        self.status_signal.connect(self.parent.actuator_status)

    def initialize(self):
        pass

    def connection(self, address=RPI_ADDR):
        if self.connected: return
        ip = address.split(":")[0]
        #os.environ['EPICS_CA_ADDR_LIST'] = str(ip)
        #os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

        try:
            self.context = Context()
            for i in range(NUMBER_OF_MONITORS):
                self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_request'] = self.context.get_pvs(f'{PV_NAME_RANK0}:{PV_NAME_RANK1}{i}:REQUEST')[0]
                self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_status'] = self.context.get_pvs(f'{PV_NAME_RANK0}:{PV_NAME_RANK1}{i}:STATUS')[0]

            time.sleep(2)
            message = f"INFO EPICS server is connected."
            self.connected = True
            if self.pvs == {}:
                self.set_monitor(self.monitor)
        except:
            message = "ERROR Connection is failed."
            self.connected = False
        finally:
            return message

    async def run(self):
        if any(i == self.request for i in [REQUEST_GO_UP, REQUEST_GO_DOWN]) and self.request != self.previous_request:
            self.pvs['request'].write(self.request)
            self.previous_request = self.request

    def stop(self):
        self.working = False
        #self.sleep(1)
        self.quit()
        self.wait(2000)

    def set_monitor(self, monitor):
        self.monitor = monitor
        if self.connected:
            self.pvs = {}
            for i in range(NUMBER_OF_MONITORS):
                if f'{PV_NAME_RANK1.lower()}{i}' == monitor.lower():
                    self.pvs['request'] = self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_request']
                    self.pvs['status'] = self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_status']

    def send_status(self):
        self.pvs['request'].write(REQUEST_STATUS)
        status = self.pvs['status'].read().data[0]
        message = ''
        if status == ACTUATOR_UP:
            message = "Screen monitor is up."
        elif status == ACTUATOR_DOWN:
            message = "Screen monitor is down."
        elif status == ACTUATOR_GOES_UP:
            message = "Screen monitor is goes up."
        elif status == ACTUATOR_GOES_DOWN:
            message = "Screen monitor is goes down."
        elif status == ACTUATOR_ERROR:
            message = "An error occured."
        self.status_signal.emit(message)

    @Slot(int)
    def receive_request(self, value):
        self.previous_request = self.request
        self.request = value
        asyncio.run(self.run())