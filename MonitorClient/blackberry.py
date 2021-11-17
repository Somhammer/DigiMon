import os, sys
import time
from PySide6.QtCore import *
from caproto.threading.client import Context

from variables import *

class Blackberry(QThread):
    status_signal = Signal(str)
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.name = "Profile Monitor Controller"

        self.working = False
        self.connected = False
        self.context = None
        self.request = None
        self.status = None
        self.previous_request_number = None
        self.request_number = None

        #self.status_signal.connect(self.parent.actuator_status)

    def initialize(self):
        pass

    def connection(self, address):
        ip, port = address.split(":")
        os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'
        if port == '':
            os.environ['EPICS_CA_ADDR_LIST'] = str(address)
        else:
            os.environ['EPICS_CA_ADDR_LIST'] = str(ip)

        try:
            self.context = Context()
            self.request, self.status = self.context.get_pvs('SCREEN-MONITOR-1:request', 'SCREEN-MONITOR-1:status')
            self.request.write(REQUEST_STATUS)
            self.send_status()
            message = f"INFO EPICS server is connected."
            self.connected = True
        except:
            message = "ERROR Connection is failed."
            self.connected = False
        finally:
            return message

    def run(self):
        while self.working:
            if any(i == self.request_number for i in [REQUEST_GO_UP, REQUEST_GO_DOWN]) and self.request_number != self.previous_request_number:  
                self.request.write(self.request_number)
            #self.request.write(REQUEST_STATUS)
            #self.send_status()
            time.sleep(1)

    def stop(self):
        self.working = False
        self.sleep(1)
        self.quit()

    def send_status(self):
        status = self.status.read().data[0]
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
        #self.status_signal.emit(message)

    @Slot(int)
    def receive_request(self, value):
        if self.previous_request_number is None:
            self.previous_request_number = value
        else:
            self.previous_request_number = self.request_number
        self.request_number = value