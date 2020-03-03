from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():

    def __init__(self, driver:webdriver.Firefox):
        '''公共参数'''
        self.driver = driver

    def find(self, locator):
        '''封装定位元素'''
        elenemt = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        return elenemt

    def finds(self, locator):
        '''封装复数定位元素'''
        elenemts = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*locator))
        return elenemts

    def send(self, locator, _text):
        '''封装点击输入框'''
        self.find(locator).send_keys(_text)

    def sends(self, locator, n, _text):
        '''封装复数点击输入框'''
        self.finds(locator)[n].send_keys(_text)

    def click(self, locator):
        '''封装点击元素'''
        self.find(locator).click()

    def clicks(self,locator, n):
        '''封装复数点击元素'''
        self.finds(locator)[n].click()

    def resutl(self, locator):
        '''获取结果的公共方法'''
        try:
            r = self.find(locator).text
        except:
            r = ""
        return r

    def move_to_elenemt(self, locator):
        '''封装鼠标悬停事件'''
        elenemt = self.find(locator)
        ActionChains(self.driver).move_to_element(elenemt).perform()

    def select_by_index(self, locator, index=0):
        '''封装select通过index定位'''
        elenemt = self.find(locator)
        Select(elenemt).select_by_index(index)

    def select_by_value(self, locator, value):
        '''封装select通过value定位'''
        elenemt = self.find(locator)
        Select(elenemt).select_by_value(value)

    def select_by_text(self, locator, _text):
        '''封装select通过text定位'''
        elenemt = self.find(locator)
        Select(elenemt).select_by_visible_text(_text)

    def switch_window(self, n):
        '''封装切换窗口动作'''
        all_h = self.driver.window_handles
        h = all_h[n]
        self.driver.switch_to.window(h)

    def switch_iframe(self, locator, n):
        '''封装切换iframe动作'''
        elenemt = self.finds(locator,)[n]
        self.driver.switch_to.frame(elenemt)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.0.113:16082/login.html")
    d = Base(driver)
    loc_0 = ("xpath", "//div[@class='skip']")
    loc_1 = ("id", "name")
    loc_2 = ("id", "password")
    loc_3 = ("id", "code")
    loc_4 = ("xpath", ".//*[text() ='登录']")
    d.click(loc_0)
    d.send(loc_1, "admin")
    d.send(loc_2, "bx84044608")
    d.send(loc_3, "8888")
    d.click(loc_4)















