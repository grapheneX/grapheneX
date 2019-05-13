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
        run_server(args['host_port'].split(':') \
            if ':' in args['host_port'] \
            else (args['host_port'], '8080'))
    else:
        start_cli()

if __name__ == "__main__":
    main()