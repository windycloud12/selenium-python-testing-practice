import logging
import os.path
import config


class LoggingFactory:
    __instance = None
    __logger = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__logger = logging.getLogger(config.LOGGER_NAME)
            cls.__logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
            #
            # console_handler = logging.StreamHandler()
            # console_handler.setLevel(logging.DEBUG)
            # console_handler.setFormatter(formatter)
            # cls.__logger.addHandler(console_handler)

            os.makedirs(config.LOG_PATH, exist_ok=True)
            log_path = os.path.join(config.LOG_PATH, config.LOG_FILE_NAME)
            file_handler = logging.FileHandler(log_path)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            cls.__logger.addHandler(file_handler)

        return cls.__instance

    def get_logger(self):
        return self.__logger


logger = LoggingFactory().get_logger()
