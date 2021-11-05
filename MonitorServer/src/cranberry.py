#===============================================================
#
#  Beam profile monitor screen control system
#
#         Original Author: Garam HAHN  <garam.hahn@gmail.com>
#                  Author: Seohyeon AN <klar.wind0425@gmail.com>
#
#===============================================================
import os, sys
import logging
import socket
import threading

import_GPIO = False
try:
    import RPi.GPIO as GPIO
    import_GPIO = True
except ImportError:
    import_GPIO = False

from src.variables import *

class Cranberry():
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.close = False
        self.set_logger()
        self.initialize_server()
        self.run_server()

    def set_logger(self):
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

    def initialize_server(self):
        self.logger.info("Initialize Cranberry Server")
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.addr, self.port))
            self.server_socket.listen()
        except:
            self.logger.error("Initialization is failed")

    def run_server(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.communicate_by_thread, args=(client_socket, addr))
            thread.start()
            thread.join()
            if self.close:
                self.server_socket.close()
                self.logger.info(f"Close the Cranberry Server")
                break

    def communicate_by_thread(self, client_socket, addr):
        self.logger.info(f"Connectd at {addr[0]}:{addr[1]}")
        if import_GPIO:
            self.set_GPIO()
        while True:
            try:
                command = client_socket.recv(1024)
                if not command: 
                    break
                self.logger.info(f"Received from {addr[0]}:{addr[1]}: {command.decode()}")
                reply = self.handle_screen(command.decode())
                client_socket.send(reply.encode())
                if any(i in command.decode().lower() for i in ['quit','exit','q']):
                    self.close = True
                    self.logger.info(f"Received the disconnect command.")
                    break
            except ConnectionError as err:
                self.logger.error(f"The connection is broken.")
                break
        
        self.logger.info(f"Disconnectd at {addr[0]}:{addr[1]}")
        if import_GPIO:
            self.close_GPIO()
        client_socket.close()

    def set_GPIO(self):
        GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
        GPIO.setup([UPPER_SWITCH, LOWER_SWITCH], GPIO.IN)
        GPIO.setup(RELAY, GPIO.OUT)

        self.last_switch = None

    def close_GPIO(self):
        GPIO.cleanup()

    def handle_screen(self, command):
        if any(command == i for i in ['up', 'down', 'status']): return ''
        reply = ""
        try:
            upper_switch_status = int(GPIO.input(UPPER_SWITCH) + 10)
            lower_switch_status = int(GPIO.input(LOWER_SWITCH) + 10)
        except:
            self.logger.exception("Switches are not connected. Please, handle the problem.")
            return reply

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
            self.logger.exception("The actuator cannot catch the position itself. Please, handle the problem.")
            return reply

        try:
            if command == 'status':
                if actuator_status == ACTUATOR_UP:
                    self.logger.info("Status: the screen is up.")
                    reply = "The screen is up."
                elif actuator_status == ACTUATOR_DOWN:
                    self.logger.info("Status: the screen is down.")
                    reply = "The screen is down."
                elif actuator_status == ACTUATOR_GOES_DOWN:
                    self.logger.info("Status: the screen goes down.")
                    reply = "The screen goes down."
                elif actuator_status == ACTUATOR_GOES_UP:
                    self.logger.info("Status: the screen goes up.")
                    reply = "The screen goes up."
            elif command == 'up':
                GPIO.output(RELAY, False)
                reply = 'The relay switch is off. The screen will be up.'
            elif command == 'down':
                GPIO.output(RELAY, True)
                reply = 'The relay switch is on. The screen will be down.'
        except:
            self.logger.exception("Problem handling request.")
            reply = f"Problem occurs while running command {command}. Please, handle the problem."
        finally:
            return reply