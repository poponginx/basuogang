from  selenium import webdriver
from common.base import Base
import time
locat_user = ('id', 'name')
locat_paw = ('id', 'password')
locat_batuut = ('xpath', ".//*[text()='登录']")
locat_reqult = ('xpath', ".//*[text()='基础信息管理']")

class LogInBaSuoGang(Base):
    '''
    登录八所港的类
    '''
    def input_user(self, user='admin'):
        '''
        用户名输入
        :param user:
        :return:
        '''
        self.send(locat_user, user)

    def input_pws(self, paw='Bsg123456admin,'):
        '''
        密码输入
        :param paw:
        :return:
        '''
        self.send(locat_paw, paw)

    def input_but(self):
        '''
        点击登录
        :return:
        '''
        self.click(locat_batuut)

    def reult(self, timeout=10):
        self.resutl(locat_reqult)

    def login_res(self, user='admin', paw='Bsg123456admin,'):
        '''
        登录函数
        :param user:
        :param paw:
        :return:
        '''
        self.send(locat_user, user)
        self.send(locat_paw, paw)
        self.click(locat_batuut)
        self.resutl(locat_reqult)

if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get('http://120.132.120.29:18066/portal/public/login.html')
    BSG = LogInBaSuoGang(driver)
    BSG.login_res()
    print('登录成功')
    driver.close()

