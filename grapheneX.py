#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header
from core.cli.shell import start_cli
from core.web.server import run_server

def main():
    args = parse_cli_args()
    print_header()
    if(args['web']):
        run_server(args)
        
    else:
        start_cli()

if __name__ == "__main__":
    main()