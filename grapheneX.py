#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header, check_privileges, parser_host_port, run_shell, run_server
from core.cli.shell import Shell
from core.web.server import *
import threading

def main():
    args = parse_cli_args()
    print_header()
    check_privileges()
    shell = Shell()
    if(args['web']):
        host, port = parser_host_port(args['host_port'])
        shell_thread = threading.Thread(target=run_shell,args=(shell,))
        web_thread = threading.Thread(target=run_server, args=(app,host,port))
        shell_thread.start()
        web_thread.start()
    else:
        run_shell(shell)


if __name__ == "__main__":
    main()