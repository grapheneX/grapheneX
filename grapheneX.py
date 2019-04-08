#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header
from core.shell import Shell

def main():
    parse_cli_args()
    print_header()

    shell = Shell()
    shell.cmdloop()

if __name__ == "__main__":
    main()
