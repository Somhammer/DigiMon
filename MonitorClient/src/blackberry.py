import os, sys
import socket
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from src.variables import *

class Blackberry():
    def __init__(self):
        self.connected = False
        self.name = "Profile Monitor Controller"

    def initialize(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((CONTROLLER_ADDR, CONTROLLER_PORT))
            self.connected = True
        except:
            return

    def send_command(self, cmd):
        self.client_socket.send(cmd.encode())
        response = self.client_socket.recv(1024)
        return repr(response.decode())