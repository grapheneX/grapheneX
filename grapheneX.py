#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.helpers import print_header
from core.logcl import GraphenexLogger

logger = GraphenexLogger("graphenex.main", level="DEBUG")

def main():
    print_header()
    logger.debug("Graphenex started")

if __name__ == "__main__":
    main()
