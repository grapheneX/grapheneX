#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header, check_privileges
from core.cli.shell import Shell
from core.web.server import run_server

def main():
    args = parse_cli_args()
    print_header()
    check_privileges()
    if(args['web']):
        run_server(args['host_port'].split(':') \
            if ':' in args['host_port'] \
            else (args['host_port'], '8080'))
    else:
        shell = Shell()
        try:
            shell.cmdloop()
        except KeyboardInterrupt:
            shell.do_EOF(None)

if __name__ == "__main__":
    main()