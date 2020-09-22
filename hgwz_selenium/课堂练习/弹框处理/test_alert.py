from time import sleep

from selenium.webdriver import ActionChains

from hgwz_test.hgwz_selenium.Base.Base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element_by_id('draggable')
        drog = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drog)
        action.perform()
        sleep(3)
        alert = self.driver.switch_to.alert.accept()  # 点击弹框中的确认；
        self.driver.switch_to.default_content()  # 返回默认窗口
        print('操作完成')
        sleep(5)
