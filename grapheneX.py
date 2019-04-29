#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header,check_admin_win,check_os
from core.cli.shell import Shell
from core.utils.logcl import GraphenexLogger
logger = GraphenexLogger(__name__)
def main():
    parse_cli_args()
    print_header()
    shell = Shell()
    if check_os():
        if not check_admin_win():
            logger.info("Do not have a administrative access please get administrative access and re-run ")
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        shell.do_EOF(None)

if __name__ == "__main__":
    main()