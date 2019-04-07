#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header

def main():
    parse_cli_args()
    print_header()

if __name__ == "__main__":
    main()
