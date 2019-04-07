#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import argparse

def cli_arg_parser():
  parser = argparse.ArgumentParser(description= \
          'grapheneX | Automated Hardening Framework')
  parser.add_argument('-w',
                    '--web', 
                    help='For Web Interface')
  args= parser.parse_args()
