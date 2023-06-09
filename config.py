import os
import datetime

from src.common.enums.webdriver_enum import WebDriverEnum

PROJECT_DIRECTORY = os.getcwd()

# Yahoo Loging info
USER_ACCOUNT = "ABC"
USER_PASSWORD = "ABC"

# Driver
DRIVER_TYPE = WebDriverEnum.FIREFOX
DRIVER_VERSION_CHROME = 111
DRIVER_ABS_PATH_CHROME = f"./resources/drivers/chromedriver{DRIVER_VERSION_CHROME}.exe"

# Log
LOGGER_NAME = 'MAINLOG'
LOG_FILE_NAME = f'{datetime.datetime.now().strftime("%Y%m%d")}.log'
LOG_PATH = f'{PROJECT_DIRECTORY}/log'

# Report
REPORT_TIMESTAMP = datetime.datetime.now()
REPORT_FOLDER_NAME = f'reports'
REPORT_FILE_NAME = f'report_{REPORT_TIMESTAMP.strftime("%Y%m%d%H%M")}.html'

# Screenshot
SCREENSHOT_FOLDER_NAME = f'screenshot_{REPORT_TIMESTAMP.strftime("%Y%m%d%H%M")}'
SCREENSHOT_DIRECTORY = os.path.join(PROJECT_DIRECTORY, REPORT_FOLDER_NAME, SCREENSHOT_FOLDER_NAME)
