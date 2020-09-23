from hgwz_test.hgwz_selenium.课堂练习.pageObject框架练习.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()
