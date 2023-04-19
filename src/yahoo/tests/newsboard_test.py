import time

import pytest

from src.common.tests.base_test_class import BaseTestClass
from src.yahoo.pages.main_page import MainPage


@pytest.mark.describe('首頁 - 新聞看版')
class TestNewboard(BaseTestClass):

    def setup(self):
        self.main_page = MainPage(self.driver)
        self.url = "https://www.yahoo.com.tw"
        self.driver.get(self.url)

    @pytest.mark.describe('檢查新聞看版重要元件的數量')
    def test_format_of_news_board(self):
        # 檢查頁籤數量
        nums = self.main_page.get_number_of_tabs()
        expected_num = 6
        assert nums == expected_num, f"結果錯誤: 頁籤期望得到 {expected_num} 個，但實際得到 {nums} 個"

        # 檢查頁籤對應的看板數量
        panel_num = self.main_page.get_number_of_panels()
        assert panel_num == expected_num, f"结果错误: 看板數量期望得到 {expected_num} 個，但實際得到 {panel_num} 個"

        # 檢查看板內的連結數量
        for idx in range(0, panel_num):
            img_num, txt_num = self.main_page.get_number_of_links(idx)
            expected_img_num = 3
            expected_txt_num = 6
            assert img_num == expected_img_num and txt_num == expected_txt_num, \
                f"结果错误: 第 {idx+1} 個看版, 期望得到 {expected_img_num} 個圖片連結和 {expected_txt_num} 個文字連結，但實際得到 {img_num} 個圖片連結和 {txt_num} 個文字連結"

    @pytest.mark.describe('檢查新聞看板的連結是否有效')
    def test_valid_of_link(self):
        # 取得連結
        links_of_each_panel = self.main_page.get_each_panel_links()

        for idx_panel, panel in enumerate(links_of_each_panel):
            for idx, link in enumerate(panel):
                assert link.is_enabled(), '結果錯誤: 新聞連結無法點擊'

    def test_board_format(self):
        self.driver.maximize_window()
        time.sleep(2)

    def test_a(self):
        self.driver.set_window_size(800, 600)
        time.sleep(2)
