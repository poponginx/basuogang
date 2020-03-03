from selenium import webdriver
from common.base import Base


locat_anniu = ('xpath', ".//*[@id='login_form']/div[5]/span[2]")#注册按钮
locat_user = ('id', 'userName')#用户名
locat_phone = ('id', 'phone')#手机号
locat_selectOrg = ('id', 'selectOrg')
locat_office = ('id', 'office')
locat_email = ('id', 'email')
locat_userpws = ('id', 'userPassword')
locat_userpws1 = ('id', 'userPassword1')
locat_zhuce = ('xpath', ".//*[@id='login_form']/div[9]/span[1]")
locat_denglu = ('xpath', ".//*[text()='登录']")
class ZhuCe(Base):
    '''
    封装注册的类
    '''
    def zhuce_anniu(self):
        '''
        点击注册按钮进入注册界面
        :return:
        '''
        self.click(locat_anniu)
    def zhuce_user(self, user='lianxi-pytest'):
        '''
        输入注册用户名称
        :param user:
        :return:
        '''
        self.send(locat_user, user)
    def zhuce_phone(self, phone='18596963205'):
        '''
        输入手机号
        :param phone:
        :return:
        '''
        self.send(locat_phone, phone)
    def zhuce_leixin(self, value='游客'):
        '''
        选择用户类型
        :param value:
        :return:
        '''
        self.select_by_value(locat_selectOrg, value)
    def zhuce_office(self, office='测试公司'):
        '''
        输入公司名称
        :param office:
        :return:
        '''
        self.send(locat_office, office)
    def zhuce_email(self, email='256217486@qq.com'):
        '''
        输入邮箱号码
        :param email:
        :return:
        '''
        self.send(locat_email, email)
    def zhuce_pws(self, pws='123456'):
        '''
        输入密码
        :param pws:
        :return:
        '''
        self.send(locat_userpws, pws)
    def zhuce_pws1(self, pws1='123456'):
        '''
        再次确认密码
        :param pws1:
        :return:
        '''
        self.send(locat_userpws1, pws1)
    def zhuce_dianji(self):
        '''
        点击注册按钮进行注册
        :return:
        '''
        self.click(locat_zhuce)
    def zhuce_suess(self) :
        '''
        加个注册成功的判断
        :return:
        '''
        self.resutl(locat_denglu)

    def zhuces(self):
        '''
        调用各个方法
        :return:
        '''
        try:
            #调用点击注册按钮方法
            zhuce.zhuce_anniu()
            #调用输入用户名方法
            zhuce.zhuce_user()
            #调用输入手机号方法
            zhuce.zhuce_phone()
            #调用选择用户类型方法
            zhuce.zhuce_leixin()
            #调用输入公司方法
            zhuce.zhuce_office()
            #调用输入邮箱方法
            zhuce.zhuce_email()
            #调用输入密码方法
            zhuce.zhuce_pws()
            #调用再次输入密码方法
            zhuce.zhuce_pws1()
            #调用注册按钮进行确定方法
            zhuce.zhuce_dianji()
            #调用注册成功后的页面方法
            zhuce.zhuce_suess()
        except Exception:
            return None

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://120.132.120.29:18066/portal/public/login.html')
    zhuce = ZhuCe(driver)
    zhuce.zhuces()
    driver.close()
