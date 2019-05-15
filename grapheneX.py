#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.argparser import parse_cli_args
from core.utils.helpers import print_header, check_privileges, parser_host_port, logger
from core.cli.shell import Shell
from core.web import app

DEBUG = True

def main():
    args = parse_cli_args()
    print_header()
    check_privileges()
    if(args['web']):
        host, port = parser_host_port(args['host_port'])
        try:
            logger.info(f'Starting Server {host}:{port}')
            app.run(host=host, port=port, debug=DEBUG)
        except:
            logger.error('Invalid host & port address')
            logger.info('Using default (host: 0.0.0.0, port: 8080)')
            logger.info('Starting Server 0.0.0.0:8080')
            app.run(host='0.0.0.0', port=8080, debug=DEBUG)
    else:
        shell = Shell()
        try:
            shell.cmdloop()
        except KeyboardInterrupt:
            shell.do_EOF(None)

if __name__ == "__main__":
    main()