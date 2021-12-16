#!/usr/bin/env python
import os, sys
import textwrap
import socket
import threading

BASE_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from caproto.server import ioc_arg_parser, run

from src.variables import *
from src.cranberry import Cranberry

if __name__ == '__main__':
    ioc_options, run_options = ioc_arg_parser(
        default_prefix=f"{PV_NAME_RANK0}:",
        desc=textwrap.dedent(Cranberry.__doc__)
    )
    ioc = Cranberry(**ioc_options)
    run(ioc.pvdb, **run_options)