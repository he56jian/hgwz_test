from appium.webdriver.webdriver import WebDriver


class BasePage:
    """
    基类：存放一些最基本的方法，
    实例化：driver，find，back,time
    """

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_send(self, locator, value):
        self.find(locator).send_keys(value)
