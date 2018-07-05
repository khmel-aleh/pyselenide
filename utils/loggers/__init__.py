from robot.api import logger as rf_logger

levels = ('TRACE', 'DEBUG', 'INFO', 'HTML', 'WARN', 'ERROR')


class Logger(object):

    def __init__(self, logger):
        self._logger = logger

    def log(self, msg, level):
        self._logger.write(msg, level)

    def debug(self, *args, **kwargs):
        self._logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        self._logger.info(*args, **kwargs)


logger = Logger(rf_logger)
