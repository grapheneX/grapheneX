#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.logcl import GraphenexLogger

logger = GraphenexLogger("graphenex.main", level="DEBUG")

def main():
    logger.debug("Graphenex started")
    print("GrapheneX")

if __name__ == "__main__":
    main()
