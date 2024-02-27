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

import os
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

    def connect_device(self):
        if self.para.ctl_conn: return
        ip = self.para.server_ip.split(":")[0]
        os.environ['EPICS_CA_ADDR_LIST'] = str(ip)
        os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'

        try:
            self.context = Context()
            for i in range(NUMBER_OF_MONITORS):
                if f'{PV_NAME_RANK1.lower()}{i}' == self.para.monitor_id.lower():
                    print(i)
                    self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_request'] = self.context.get_pvs(f'{PV_NAME_RANK0}:{PV_NAME_RANK1}{i}:REQUEST')[0]
                    self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_status'] = self.context.get_pvs(f'{PV_NAME_RANK0}:{PV_NAME_RANK1}{i}:STATUS')[0]

                    time.sleep(2)
                    print("MELONA")
                    self.pvs['request'] = self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_request']
                    self.pvs['status'] = self.__dict__[f'{PV_NAME_RANK1.lower()}{i}_status']
            
            print("MELONA")
            print(f"{self.pvs['status'].read()}")
            #message = f"INFO EPICS server is connected. {self.para.monitor_id} Status: {self.status_to_text(self.pvs['status'].read().data[0])}"
            message = f"INFO MELONA"
            self.para.ctl_conn = True
            print("MELONA")
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
            elif self.request == ACTUATOR_REQUEST_STATUS:
                self.send_status()

    def stop(self):
        self.working = False
        self.quit()
        self.wait(1000)

    def status_to_text(self, status):
        if status == ACTUATOR_UP:
            text = "Screen Up"
        elif status == ACTUATOR_DOWN:
            text = "Screen Down"
        elif status == ACTUATOR_GOES_UP:
            text = "Go up"
        elif status == ACTUATOR_GOES_DOWN:
            text = "Go down"
        elif status == ACTUATOR_ERROR:
            text = "Error"
        return text

    def send_status(self):
        self.pvs['request'].write(ACTUATOR_REQUEST_STATUS)
        message = self.status_to_text(self.pvs['status'].read().data[0])
        self.status_signal.emit(message)

    @Slot(int)
    def receive_request(self, value):
        self.previous_request = self.request
        self.request = value
        asyncio.run(self.run())