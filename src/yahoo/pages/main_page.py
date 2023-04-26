from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from src.common.tests.base_page import BasePage


class Locator:
    NEWS_TABS = (By.XPATH,
                 "//div[@id='applet_p_50000313']/div/div[contains(@class,'tabs-header')]/ul[contains(@class,'tabs-list')]/li")
    NEWS_PANELS = (By.XPATH, "//div[@id='applet_p_50000313']//ul[contains(@class,'panels')]/li")
    NEWS_PANEL_IMAGE_LINK = (By.XPATH, "./div[contains(@id, '-content')]/div/div/ul/li/a")
    NEWS_PANEL_TEXT_LINK = (By.XPATH, "./div[contains(@id, '-content')]/div/ul/li/a")
    LOGIN_LINK = (By.ID, "header-signin-link")
    USER_PROFILE_BTN = (By.ID, "header-profile-button")


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_number_of_tabs(self):
        elms = self.driver.find_elements(*Locator.NEWS_TABS)
        return len(elms)

    def get_number_of_panels(self):
        elms = self.driver.find_elements(*Locator.NEWS_PANELS)
        return len(elms)

    def get_number_of_links(self, panel_order):
        elm = self.driver.find_elements(*Locator.NEWS_PANELS)[panel_order]
        num_of_img = len(elm.find_elements(*Locator.NEWS_PANEL_IMAGE_LINK))
        num_of_txt = len(elm.find_elements(*Locator.NEWS_PANEL_TEXT_LINK))
        return num_of_img, num_of_txt

    def get_each_panel_links(self):
        elms = self.driver.find_elements(*Locator.NEWS_PANELS)

        panels = []
        for idx in range(0, len(elms)):
            links_of_img = elms[idx].find_elements(*Locator.NEWS_PANEL_IMAGE_LINK)
            links_of_txt = elms[idx].find_elements(*Locator.NEWS_PANEL_TEXT_LINK)

            links = []
            links.extend(links_of_img)
            links.extend(links_of_txt)
            panels.append(links)

        return panels

    def click_login_btn(self):
        elm = self.driver.find_element(*Locator.LOGIN_LINK)
        elm.click()

    def check_login_success(self):
        try:
            elm = self.driver.find_element(*Locator.USER_PROFILE_BTN)
            return True
        except NoSuchElementException:
            return False
