
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_tab_id(self):
        return self.driver.current_window_handle

    def get_new_tab_id(self):
        self.driver.execute_script("window.open('about:blank', 'new_tab')")
        new_tab_id = self.driver.window_handles[-1]
        return new_tab_id

    def switch_to(self, target_tab_id):
        self.driver.switch_to.window(target_tab_id)

    def close_tab(self, target_tab_id):
        self.driver.switch_to.window(target_tab_id)
        self.driver.close()

    def check_valid_link(self, url):
        self.driver.get(url)
