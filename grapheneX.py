#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header, is_root, check_os
from core.cli.shell import Shell
from core.utils.logcl import GraphenexLogger

logger = GraphenexLogger(__name__)

def main():
    parse_cli_args()
    print_header()

    if not check_os():
        if not is_root():
            logger.warn('Some functions won\'t work without root access, try running the script with sudo.')

    shell = Shell()
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        shell.do_EOF(None)

if __name__ == "__main__":
    main()