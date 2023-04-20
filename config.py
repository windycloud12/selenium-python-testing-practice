import os
import datetime

from src.common.enums.webdriver_enum import WebDriverEnum

PROJECT_DIRECTORY = os.getcwd()

DRIVER_TYPE = WebDriverEnum.CHROME
DRIVER_VERSION_CHROME = 111
DRIVER_ABS_PATH_CHROME = f"./resources/drivers/chromedriver{DRIVER_VERSION_CHROME}.exe"

# Log
LOGGER_NAME = 'MAINLOG'
LOG_FILE_NAME = f'{datetime.datetime.now().strftime("%Y%m%d")}.log'
LOG_PATH = f'{PROJECT_DIRECTORY}/log'
