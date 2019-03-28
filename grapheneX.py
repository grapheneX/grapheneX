#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.logcl import GraphenexLogger

def main():
    logger = GraphenexLogger("graphenex.main", level='DEBUG')
    logger.debug("debug message")
    logger.error("Error message")

    print("GrapheneX")

if __name__ == "__main__":
    main()
