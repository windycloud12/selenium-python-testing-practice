import os

from src.common.enums.webdriver_enum import WebDriverEnum

PROJECT_DIRECTORY = os.getcwd()

DRIVER_TYPE = WebDriverEnum.CHROME
DRIVER_VERSION_CHROME = 111
DRIVER_ABS_PATH_CHROME = f"./resources/drivers/chromedriver{DRIVER_VERSION_CHROME}.exe"
