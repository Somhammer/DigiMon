import logging

from variables import *

class LogStringHandler(logging.Handler):
    def __init__(self, target_widget):
        super().__init__()
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.setFormatter(formatter)
        self.target_widget = target_widget

    def emit(self, record):
        self.format(record)
        self.target_widget.append(f'[{record.asctime}][{record.levelname}]: {record.getMessage()}')