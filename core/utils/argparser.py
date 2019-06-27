#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import argparse


def parse_cli_args():
    """
    Command-line argument parser.

    Returns parsed args as dict.
    [-w, --web]: Runs web server if given.
    """
    parser = argparse.ArgumentParser(
        description='grapheneX | Automated System Hardening Framework')
    parser.add_argument('-w',
                        '--web',
                        help='run the grapheneX web server',
                        action="store_true")
    parser.add_argument('host_port', metavar='host:port', type=str, nargs='?', 
                        default='0.0.0.0:8080',
                        help="host and port to run the web interface")
    parser.add_argument('--open', action="store_true",
                        help="open browser on web server start")
    args = vars(parser.parse_args())
    return args
