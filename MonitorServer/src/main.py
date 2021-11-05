#!/usr/bin/env python
import os, sys
import textwrap

BASE_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from src.variables import *
from src.cranberry import *

if __name__ == '__main__':
    opt = input("...Choose server connection type: tcp/ca")
    if not any(str(opt).lower() == i for i in ['tcp', 'ca']):
        print(f"Wrong option: {str(opt)}")
        sys.exit()
    if str(opt).lower() == 'tcp':
        from src.cranberry import *
        server = Cranberry(HOST_ADDR, HOST_PORT)
    elif str(opt).lower() == 'ca':
        from src.strawberry import *
        ioc_options, run_options = ioc_arg_parser(
            default_prefix='SCREEN-MONITOR-1:',
            desc=textwrap.dedent(Strawberry.__doc__)
        )
        ioc = Strawberry(**ioc_options)
        ioc.initialize()
        run(ioc.pvdb, **run_options)
