#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import logging
import sys

class GraphenexLogger(logging.Logger):
    """
    Logger class for printing logs to command-line.

    Usage:
        ```
        logger = GraphenexLogger("app", level="DEBUG")
        logger.debug("This is a debug message")
        logger.info("Cool information message")
        ```
    `GraphenexLogger(name, level, format)`
    """

    LEVELS = {
        'DEBUG': logging.DEBUG,
        'ERROR': logging.ERROR,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING
    }

    def __init__(self, name, level='INFO',
                 format="%(asctime)s > %(name)s > %(levelname)s > %(message)s"):
        # Import coloredlogs
        self.import_clogs()

        # Initial construct.
        self.format = format
        self.level = level
        self.name = name

        # Logging conf
        self.console_formatter = logging.Formatter(
            self.format, datefmt="%H:%M:%S")
        self.console_logger = logging.StreamHandler(sys.stdout)
        self.console_logger.setFormatter(self.console_formatter)

        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(GraphenexLogger.LEVELS[self.level])
        self.logger.addHandler(self.console_logger)

        # Color support
        FIELD_STYLES = dict(
            asctime=dict(color='green'),
            hostname=dict(color='magenta'),
            levelname=dict(color='cyan', bold=coloredlogs.CAN_USE_BOLD_FONT),
            filename=dict(color='magenta'),
            name=dict(color='blue'),
            threadName=dict(color='green')
        )
        coloredlogs.install(level=self.level, fmt=self.format,
                            datefmt="%H:%M:%S", logger=self.logger, 
                            field_styles=FIELD_STYLES)

    def import_clogs(self):
        try:
            global coloredlogs
            import coloredlogs
        except:
            print("coloredlogs module not found.\n" +
                  "Install requirements.txt with pip.")
            sys.exit()

    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warn(msg, extra=extra)
