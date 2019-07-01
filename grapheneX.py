#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.helpers import parse_cli_args, print_header
from core.utils.logcl import GraphenexLogger
from core.cli.shell import start_cli
from core.web import run_server

logger = GraphenexLogger('Graphenex')

def main():
    args = parse_cli_args()
    print_header()
    if(args['web']):
        run_server(args)
    else:
        if args['open']:
            logger.warn("--open argument is unnecessary. Use with -w or --web")
        start_cli()

if __name__ == "__main__":
    main()