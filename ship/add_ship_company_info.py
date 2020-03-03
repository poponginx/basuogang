from selenium import webdriver
from common.base import Base
from ship.login import LogInBaSuoGang
import time

locat_jichu = ('xpath', ".//*[text()='基础信息管理']")#基础信息管理
locat_com_ship = ('xpath', ".//*[@id='common-bx-auth']/body/div[2]/div[1]/div[2]/p")#船务公司管理
locat_ship = ('xpath', ".//*[text()='船务公司']")#船务公司
locat_tianjia = ('id', "addBtn")#添加
locat_commpany_name = ('id', 'company_name')#船务公司名称
locat_leading_cadre = ('id', 'leading_cadre')#公司法人
locat_legal_person = ('id', 'legal_person')#负责人
locat_phone = ('id', "phone")#负责人电话
locat_registered_address = ('id', 'registered_address')#注册地址
locat_email = ('id', 'email')#负责人邮箱
locat_establishment_date = ('id', 'establishment_date')#成立日期
locat_xianzai = ('xpath', ".//*[text()='现在']")#成立日期
locat_paid_capital = ('id', "paid_capital")#实缴资本(万元)
locat_rn = ('id', 'rn')#工商注册号
locat_business_scope = ('id', "business_scope")#经营范围
locat_organizational_code = ('id', 'organizational_code')#组织机构代码
locat_registered_capital = ('id', 'registered_capital')#注册资本(万元)
locat_shxydm = ('id', 'shxydm')#社会信用代码
locat_nsrsbh = ('id', 'nsrsbh')#纳税人识别号
locat_industry = ('id', "industry")#行业
locat_quedin = ('xpath', "//*[@id='safeTrain-edit-form']/div[2]/button[1]")#确定按钮
class Ship(Base):
    '''
    添加船务公司
    '''
    def login_1(self):
        '''
        调用登录八所港函数
        :return:
        '''
        login.input_user()
        login.input_pws()
        login.input_but()
        login.reult(timeout=10)
    def add_comship(self, timeout=10):
        try:
            self.login_1()
            print('登录八所港成功')
            self.click(locat_jichu)
            self.click(locat_com_ship)
            time.sleep(2)
            self.click(locat_ship)
            self.click(locat_tianjia)
            self.send(locat_commpany_name, "test1")
            self.send(locat_leading_cadre, "test2")
            self.send(locat_legal_person, "test3")
            self.send(locat_phone, "15925256980")
            self.send(locat_registered_address, "test4")
            self.send(locat_email, "2654656@sunc.com")
            self.click(locat_establishment_date)
            self.click(locat_xianzai)
            self.send(locat_paid_capital, "258")
            self.send(locat_rn, "335211000004843")
            self.send(locat_business_scope, "test5")
            self.send(locat_organizational_code, "74737612-8")
            self.send(locat_registered_capital, "268")
            self.send(locat_shxydm, "91330211747356128R")
            self.send(locat_nsrsbh, "91330211747356128R")
            self.select_by_value(locat_industry, "J")
            # self.click(locat_quedin)
        except Exception as e:
            print('出现错误，错误为%s'%e)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://120.132.120.29:18066/portal/public/login.html')
    login = LogInBaSuoGang(driver)
    ship = Ship(driver)
    ship.add_comship(timeout=10)
    driver.close()