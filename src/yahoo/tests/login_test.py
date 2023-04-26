import pytest

import config
from src.common.tests.base_test_class import BaseTestClass
from src.common.utils.logging_factory import logger
from src.yahoo.pages.login_page import LoginPage
from src.yahoo.pages.main_page import MainPage


class TestLogin(BaseTestClass):
    main_page = MainPage(None)
    login_page = LoginPage(None)

    @classmethod
    def setup_class(cls):
        logger.info(f'開始 - {cls.__name__}')
        cls.url = "https://www.yahoo.com.tw"

    @classmethod
    def teardown_class(cls):
        logger.info(f'結束 - {cls.__name__}')

    def setup(self):
        if self.__class__.main_page.driver is None:
            self.__class__.main_page = MainPage(self.driver)

        if self.__class__.login_page.driver is None:
            self.__class__.login_page = LoginPage(self.driver)

    data_login = [
        pytest.param({"acct": "ABC", "pwd": "", "case": "測試帳號錯誤的顯示是否正常"}, id="帳號輸入錯誤",
                     marks=pytest.mark.xfail(strict=True)),
        pytest.param({"acct": config.USER_ACCOUNT, "pwd": "ABC", "case": "測試密碼錯誤的顯示是否正常"},
                     id="密碼輸入錯誤", marks=pytest.mark.xfail(strict=True)),
        pytest.param({"acct": config.USER_ACCOUNT, "pwd": config.USER_PASSWORD, "case": "測試登入是否正常"},
                     id="成功登入")
    ]

    @pytest.mark.parametrize("params_login", data_login)
    def test_login(self, params_login):
        """測試登入流程"""
        self.driver.get(self.url)
        self.main_page.click_login_btn()

        logger.info(f"測試項目: {params_login['case']}")

        # 輸入帳號
        logger.info("輸入帳號")
        ok_acct, err_msg = self.login_page.send_account(params_login["acct"])
        assert ok_acct, f'帳號:{params_login["acct"]} => {err_msg}'

        # 輸入密碼
        logger.info("輸入密碼")
        ok_pwd, err_msg = self.login_page.send_password(params_login["pwd"])
        assert ok_pwd, f'密碼:{params_login["pwd"]} => {err_msg}'

        ok_login = self.main_page.check_login_success()
        assert ok_login, f'帳號:{params_login["acct"]}, 密碼:{params_login["pwd"]} => 登入失敗'
        logger.info("登入成功")
