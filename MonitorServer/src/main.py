#!/usr/bin/env python
import os, sys

BASE_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from src.variables import *
from src.cranberry import *

if __name__ == '__main__':
    server = Cranberry(HOST_ADDR, HOST_PORT)