def connect_camera(self):
    self.para.sdk = self.comboSDKType.currentText()
    self.para.url = self.lineCameraAddr.text()

    if self.para.sdk == '' or self.para.url == '': return
    
    self.logger.info(f"Set SDK as {self.para.sdk}.")
    self.logger.info(f"Connect to {self.para.url}.")

    if self.para.cam_conn:
        self.logger.info(f"Network camera is already connected.")
        self.set_checked(self.checkCameraConnected, self.para.cam_conn)
    else:
        message = self.blueberry.connect_device()

        if 'ERROR ' in message:
            message = message.replace('ERROR ','')
            self.logger.error(message)
        elif 'INFO ' in message:
            message  = message.replace('INFO ','')
            self.logger.info(message)
    
    self.set_checked(self.checkCameraConnected, self.para.cam_conn)
    self.set_checked(self.checkConnection, self.para.cam_conn)

    if self.para.cam_conn:
        self.take_a_picture()

def disconnect_camera(self):
    if self.para.cam_conn:
        self.blueberry.stop()
        self.blueberry.disconnect_device()
    else: return

def connect_server(self):
    if self.para.server_ip =='': return
    if not self.checkUseControlServer.isChecked():
        self.logger.warning(f"Please, check 'Use Network Camera Controller Server' first.")
        return

    ip1, ip2, ip3, ip4, port = self.lineControllerIP1, self.lineControllerIP2, self.lineControllerIP3, self.lineControllerIP4, self.lineControllerIP5
    if any(i.text() == '' for i in [ip1, ip2, ip3, ip4]): return
    self.para.server_ip = '.'.join(i.text() for i in [ip1, ip2, ip3, ip4])+':'+port.text()
    self.logger.info(f"Connect to controller server at {self.para.url}.")
    self.para.monitor_id = self.comboMonitor.currentText()
    if self.para.monitor_id is None or self.para.monitor_id == '':
        self.logger.info(f'Select a profile monitor number.')
        self.para.server_ip = ''
        return

    if self.para.ctl_conn:
        self.logger.info(f"Network camera is already connected.")
        self.set_checked(self.checkControllerConnected, self.para.ctl_conn)
    else:
        message = self.blackberry.connect_device()

        if 'ERROR ' in message:
            message = message.replace('ERROR ','')
            self.logger.error(message)
        elif 'INFO ' in message:
            message  = message.replace('INFO ','')
            self.logger.info(message)
    
    self.set_checked(self.checkControllerConnected, self.para.ctl_conn)

def disconnect_server(self):
    if self.para.cam_conn:
        self.blackberry.stop()
        self.blackberry.disconnect_device()
    else: return