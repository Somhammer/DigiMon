import os, sys
import socket
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from src.variables import *

class Blackberry():
    def __init__(self):
        self.address = '127.0.0.1'
        self.port = 8000
        self.connected = False
        self.name = "Profile Monitor Controller"

    def initialize(self, addr, port):
        self.address = addr
        self.port = port
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if self.port == '':
                self.client_socket.connect((self.address))
            else:
                self.client_socket.connect((self.address, int(self.port)))
            self.connected = True
        except:
            return

    def send_command(self, cmd):
        if not self.connected:
            return
        self.client_socket.send(cmd.encode())
        response = self.client_socket.recv(1024)
        return repr(response.decode())