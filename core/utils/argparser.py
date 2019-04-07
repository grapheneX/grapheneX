#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import argparse

def parse_cli_args():
  """
  Command-line argument parser.

  Returns parsed args as dict.
  [-w, --web]: Runs web server if given.
  """
  parser = argparse.ArgumentParser(description= \
          'grapheneX | Automated System Hardening Framework')
  parser.add_argument('-w',
                    '--web', 
                    help='run grapheneX web server')
  args = vars(parser.parse_args())
  return args
  