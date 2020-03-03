#!/usr/bin/env python3
# coding:utf-8

'''
    添加船舶
'''

from selenium import webdriver
from common.base import Base
from ship.login import LogInBaSuoGang
from time import sleep
import logging

locat_jichu = ('xpath', ".//*[text()='基础信息管理']")#基础信息管理
locat_com_ship = ('xpath', ".//*[@id='common-bx-auth']/body/div[2]/div[1]/div[3]/p")#船舶信息管理
locat_ship = ('xpath', ".//*[@id='common-bx-auth']/body/div[2]/div[1]/div[3]/div/a")#船舶信息
locat_tianjia = ('id', "addBtn")#添加
locat_name = ('id', 'name')#*船名
locat_legal_person = ('id', 'legal_person')#*船舶经营人
locat_ship_width = ('id', 'ship_width')#船宽(m)
locat_nationality = ('id', 'nationality')#*国籍/船籍港
locat_classification_society = ('id', 'classification_society')#船级社
locat_ship_long = ('id', 'ship_long')#船长(m)
locat_getCompany = ('id', 'getCompany')#选择
locat_gonsi = ('xpath', "//*[@id='table_jg']/tbody/tr[1]/td[1]/input")#选择公司
locat_quedin = ('xpath', ".//*[@id='common-bx-auth']/body/div[4]/div[3]/input[1]")#点击确定
locat_delivery_date = ('name', "delivery_date")#交船日期01
locat_xianzai = ('xpath', ".//*[text()='现在']")#交船日期02

class Add_Ship(Base):
    '''
    添加船舶
    '''

    def locat_jichu(self):
        '''
        点击基础信息管理
        :return:
        '''
        self.click(locat_jichu)

    def locat_com_ship(self):
        self.click(locat_com_ship)
        sleep(1)

    def locat_ship(self):
        self.click(locat_ship)

    def locat_tianjia(self):
        self.click(locat_tianjia)

    def locat_name(self, name='lianxi-pytest'):
        self.send(locat_name, name)

    def locat_legal_person(self, legal_person='lianxi-pytest'):
        self.send(locat_legal_person, legal_person)

    def locat_ship_widt(self, ship_width='255'):
        self.send(locat_ship_width, ship_width)

    def add_ship(self, timeout=20):
        try:
            self.click(locat_jichu)
            self.click(locat_com_ship)
            # sleep(2)
            self.click(locat_ship)
            self.click(locat_tianjia)
            self.send(locat_name, 'lianxi-pytest')
            self.send(locat_legal_person, 'lianxi-pytest')
            self.send(locat_ship_width, '255')
            self.click(locat_getCompany)
            self.click(locat_gonsi)
            self.click(locat_quedin)
            self.click(locat_delivery_date)
            self.click(locat_xianzai)
        except Exception as e:
            print('出现错误，错误为%s'%e)
            logging.exception(e)


if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get('http://120.132.120.29:18066/portal/public/login.html')
    login = LogInBaSuoGang(driver)  
    ship = Add_Ship(driver)
    try:
        login.login_res()
        print('登录成功')
        ship.add_ship()
        print('添加船舶成功')
    except Exception as e:
        print('出现错误，错误信息是：%s'%e)
    # driver.close()
























