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
        while True:
            try:
                command = client_socket.recv(1024)
                if not command: 
                    break
                self.logger.info(f"Received from {addr[0]}:{addr[1]}: {command.decode()}")
                #reply = self.simple_test(command)
                reply = self.rpi_test(command.decode())
                #reply = self.handle_screen(command.decode())
                client_socket.send(reply)
                if any(i in command.decode().lower() for i in ['quit','exit','q']):
                    self.close = True
                    break
            except ConnectionResetError as err:
                break
        
        self.logger.info(f"Disconnectd at {addr[0]}:{addr[1]}")
        client_socket.close()

    def simple_test(self, command):
        return command

    def rpi_test(self, command):
        import time
        import RPi.GPIO as GPIO

        GPIO.setmode(GPIO.BCM)
        LED = 17
        SWITCH = 27
        GPIO.setup(SWITCH, GPIO.IN)
        GPIO.setup(LED, GPIO.OUT)
        reply = ''
        try:
            switch = GPIO.input(SWITCH)
            if switch:
                while(True):
                    status = GPIO.input(SWITCH)
                    if status != 1:
                        break
                    GPIO.output(LED, True)
                    time.sleep(2)
                    GPIO.output(LED, False)
                    time.sleep(2)

            if command == 'up':
                try:
                    GPIO.output(LED, True)
                    reply = 'Turn on the led'
                except:
                    reply = 'Fail to turn on the led'
            elif command == 'down':
                try:
                    GPIO.output(LED, False)
                    reply = 'Turun off the led'
                except:
                    reply = 'Fail to turn off the led'
        except:
            self.logger.exception("Problem handling request")
        finally:
            GPIO.output(LED, False)
            return reply

    def handle_screen(self, command):
        import RPi.GPIO as GPIO

        GPIO.setmode(GPIO.BCM)
        GPIO.setup([LU, LD], GPIO.IN)
        GPIO.setup(SOLVAL, GPIO.OUT)
        GPIO.output(SOLVAL, False)

        def actuator_status():
            LU_status = GPIO.input(LU)
            LD_status = GPIO.input(LD)
            if LU_status == 1 and LD_status == 1:
                return 'middle'
            elif LU_status == 0 and LD_status == 1:
                return 'down'
            elif LU_status == 1 and LD_status == 0:
                return 'up'
            else:
                return 'error'

        reply = ''
        try:
            if command == 'status':
                reply = actuator_status()
            elif command == 'up':
                try:
                    GPIO.output(SOLVAL, False)
                    reply = 'ok'
                except:
                    reply = 'no'
            elif command == 'down':
                try:
                    GPIO.output(SOLVAL, True)
                    reply = 'ok'
                except:
                    reply = 'no'
        except:
            self.logger.exception("Problem handling request")
        finally:
            return reply