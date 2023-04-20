import pytest
import config
from selenium import webdriver
from src.common.enums.webdriver_enum import WebDriverEnum
from selenium.webdriver.chrome.service import Service
from src.common.utils.logging_factory import logger


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    logger.info('===========================================')


@pytest.fixture(scope="class")
def browser(request):
    match config.DRIVER_TYPE:
        case WebDriverEnum.CHROME:
            service = Service(config.DRIVER_ABS_PATH_CHROME)
            driver = webdriver.Chrome(service=service)
        case WebDriverEnum.FIREFOX:
            driver = webdriver.Firefox()
        case WebDriverEnum.SAFARI:
            driver = webdriver.Safari()
        case WebDriverEnum.EDGE:
            driver = webdriver.Edge()
        case _:
            driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()
