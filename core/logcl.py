import logging, sys, coloredlogs

class GraphenexLogger(logging.Logger):
    LEVELS = {
        'DEBUG': logging.DEBUG,
        'ERROR': logging.ERROR,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'CRITICAL': logging.CRITICAL
    }
    def __init__(self, name, level='INFO', format="%(asctime)s | %(levelname)s | %(message)s"):
        # Initial construct.
        self.format = format
        self.level = level
        self.name = name

        # Logging conf
        self.console_formatter = logging.Formatter(self.format, datefmt="%H:%M:%S")
        self.console_logger = logging.StreamHandler(sys.stdout)
        self.console_logger.setFormatter(self.console_formatter)
 
        self.logger = logging.getLogger("Graphenex")
        self.logger.setLevel(GraphenexLogger.LEVELS[self.level])
        self.logger.addHandler(self.console_logger)

        # Color support
        coloredlogs.install(level=self.level, fmt=self.format, datefmt="%H:%M:%S", logger=self.logger)

    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warn(msg, extra=extra)