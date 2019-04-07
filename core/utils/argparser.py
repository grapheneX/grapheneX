#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import argparse

def parse_cli_args():
  parser = argparse.ArgumentParser(description= \
          'grapheneX | Automated Hardening Framework')
  parser.add_argument('-w',
                    '--web', 
                    help='For Web Interface')
  args= parser.parse_args()
