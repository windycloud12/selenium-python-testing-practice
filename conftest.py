import pytest
import config as config_doc
import selenium
import os
from selenium import webdriver
from src.common.enums.webdriver_enum import WebDriverEnum
from selenium.webdriver.chrome.service import Service
from src.common.utils.logging_factory import logger
from py.xml import html
from platform import python_version


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    logger.info('===========================================')


driver_version = None


@pytest.fixture(scope="class")
def browser(request):
    match config_doc.DRIVER_TYPE:
        case WebDriverEnum.CHROME:
            service = Service(config_doc.DRIVER_ABS_PATH_CHROME)
            driver = webdriver.Chrome(service=service)
        case WebDriverEnum.FIREFOX:
            driver = webdriver.Firefox()
        case WebDriverEnum.SAFARI:
            driver = webdriver.Safari()
        case WebDriverEnum.EDGE:
            driver = webdriver.Edge()
        case _:
            driver = webdriver.Firefox()

    global driver_version
    driver_version = driver.execute_script("return navigator.userAgent;")
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_html_report_title(report):
    report.title = "測試報告"


# 顯示環境
def pytest_configure(config):
    config._metadata.clear()
    config._metadata['測試項目'] = "項目名"
    config._metadata['測試地址'] = "網頁連結"
    config._metadata['Python 版本'] = python_version()
    config._metadata['Selenium 版本'] = selenium.__version__
    config._metadata['瀏覽器'] = config_doc.DRIVER_TYPE.name
    config.option.htmlpath = os.path.join(config_doc.REPORT_FOLDER_NAME, config_doc.REPORT_FILE_NAME)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    global driver_version
    session.config._metadata["瀏覽器版本"] = driver_version
    session.config._metadata.pop("Base URL")
    session.config._metadata.pop("Capabilities")
    session.config._metadata.pop("Driver")


def pytest_collection_modifyitems(items):
    for item in items:
        # 中文要轉碼, 在 console 才不會亂碼
        item.name = item.name.encode('utf-8').decode('unicode-escape')

        # 中文要轉碼, 在 IDE 測試介面才不會亂碼
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear()
    prefix.extend([html.p("測試負責人: 張OO")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.pop()
    cells.insert(2, html.th('Description', class_="sortable", col="description"))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.pop()
    custom_description = getattr(report, "test_description", "")
    cells.insert(2, html.td(custom_description, class_="col-description"))

    # 由於前面有轉碼過, 這裡要轉回來, 否則經過 pytest_html\result.py 再次轉碼後會變成亂碼
    cells[1][0] = cells[1][0].encode('latin1').decode('utf-8')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # 將函數的三個雙引號說明欄, 寫入報告裡
    report.test_description = item.function.__doc__

    if report.when == "call":
        if not report.passed:
            if not os.path.exists(config_doc.SCREENSHOT_DIRECTORY):
                os.mkdir(config_doc.SCREENSHOT_DIRECTORY)

            shot_name = report.head_line.replace(".", "_")+".png"
            shot_full_path = os.path.join(config_doc.SCREENSHOT_DIRECTORY, shot_name)

            shot_ok = item.cls.driver.get_screenshot_as_file(shot_full_path)
            pytest_html = item.config.pluginmanager.getplugin("html")

            if shot_ok:
                report.extra.append(pytest_html.extras.image(shot_full_path))
            else:
                report.extra.append(pytest_html.extras.text('截圖失敗'))
