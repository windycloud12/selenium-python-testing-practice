import pytest


@pytest.mark.usefixtures("browser")
class BaseTestClass:
    def setup(self):
        print("BaseTestClass")
        pass


