from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from src.common.tests.base_page import BasePage


class Locator:
    OTHER_ACCOUNT_LINK = (By.XPATH, "//div[@class='bottom-cta']/a")
    LOGIN_USERNAME_INPUT = (By.ID, "login-username")
    LOGIN_PASSWORD_INPUT = (By.ID, "login-passwd")
    NEXT_STEP_BTN = (By.ID, "login-signin")
    USER_ERROR_MSG = (By.ID, "username-error")
    ERROR_MSG = (By.CLASS_NAME, "error-msg")


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_if_exist_account(self):
        elm = self.driver.find_elements(*Locator.OTHER_ACCOUNT_LINK)
        if elm:
            elm.click()

    def send_account(self, acct):
        self.click_if_exist_account()
        elm_input = self.driver.find_element(*Locator.LOGIN_USERNAME_INPUT)
        elm_nxt_btn = self.driver.find_element(*Locator.NEXT_STEP_BTN)

        if elm_input and elm_nxt_btn:
            elm_input.send_keys(acct)
            elm_nxt_btn.click()

            acct_ok, error_msg = self.check_account()
            if acct_ok:
                return True, ""
            else:
                return acct_ok, error_msg

        else:
            return False, "取得元素失敗"

    def send_password(self, pwd):
        elm_pwd = self.driver.find_element(*Locator.LOGIN_PASSWORD_INPUT)
        elm_nxt_btn = self.driver.find_element(*Locator.NEXT_STEP_BTN)

        if elm_pwd and elm_nxt_btn:
            elm_pwd.send_keys(pwd)
            elm_nxt_btn.click()

            pwd_ok, error_msg = self.check_password()
            if pwd_ok:
                return True, ""
            else:
                return pwd_ok, error_msg

        else:
            return False, "取得元素失敗"

    def check_account(self):
        try:
            elm = self.driver.find_element(*Locator.USER_ERROR_MSG)
            return False, elm.text
        except NoSuchElementException:
            return True, ""

    def check_password(self):
        try:
            elm = self.driver.find_element(*Locator.ERROR_MSG)
            return False, elm.text
        except NoSuchElementException:
            return True, ""
