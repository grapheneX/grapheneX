#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header,check_admin_win
from core.cli.shell import Shell
logger = GraphenexLogger(__name__)
def main():
    parse_cli_args()
    print_header()
    shell = Shell()
    check_admin_win()
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        shell.do_EOF(None)

if __name__ == "__main__":
    main()