# -------------------------------------------------------
# Blackberry
# Author: Seohyeon An
# Date: 2022-04-21
#
# This class controls the network camera.
#   Functions
#   1. It connects the client and the network camera.
#   2. It captures images and sends them to stream_queue or analyze_queue.
# -------------------------------------------------------

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
    def __init__(self, para, main):
        super().__init__()
        self.para = para
        self.main = main
        self.name = "Profile Monitor Controller"

        self.working = False
        self.pvs = {}
        self.context = None
        self.request = None
        self.status = None
        self.previous_request = None
        self.request = None

        self.status_signal.connect(self.main.actuator_status)

    def connection_device(self, address=RPI_ADDR):
        if self.para.ctl_conn: return
        ip = address.split(":")[0]
        os.environ['EPICS_CA_ADDR_LIST'] = str(ip)
        os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

        try:
            self.context = Context()
            for i in range(NUMBER_OF_MONITORS):
                if f'{PV_NAME_RANK1.lower()}{i}' == self.para.monitor_id.lower():
                    self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_request'] = self.context.get_pvs(f'{PV_NAME_RANK0}:{PV_NAME_RANK1}{i}:REQUEST')[0]
                    self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_status'] = self.context.get_pvs(f'{PV_NAME_RANK0}:{PV_NAME_RANK1}{i}:STATUS')[0]

                    time.sleep(2)

                    self.pvs['request'] = self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_request']
                    self.pvs['status'] = self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_status']
        
            message = f"INFO EPICS server is connected."
            self.para.ctl_conn = True

        except:
            message = "ERROR Connection is failed."
            self.para.ctl_conn = False
        finally:
            return message

    def disconnect_device(self):
        self.pvs = {}
        self.para.ctl_conn = False

    async def run(self):
        if self.para.monitor_id != '':
            if any(i == self.request for i in [ACTUATOR_REQUEST_GO_UP, ACTUATOR_REQUEST_GO_DOWN]) and self.request != self.previous_request:
                self.pvs['request'].write(self.request)                
                t = 0
                while t <= 6:
                    self.send_status()
                    t += 2
                    time.sleep(2)
                self.previous_request = self.request

    def stop(self):
        self.working = False
        self.quit()
        self.wait(2000)

    def send_status(self):
        self.pvs['request'].write(ACTUATOR_REQUEST_STATUS)
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