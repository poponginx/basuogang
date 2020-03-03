# coding:utf-8
import requests
import re
# 禅道登录案例


def is_login_sucess():
    '''
     判断是否登录成功
     :param loginRes: 登录函数返回的内容
     :return: Ture or False
     '''
    if "登录失败" in loginRes:
        print("登录失败了！")
        return False
    elif"parent.location=" in loginRes:
        print("登录成功了")
        return True
    else:
        print("出现了其它的返回结果，登录失败！")
        return False

def login(s, user, psw):

    url = "http://192.168.0.138/zentao/user-login.html"
    hear = {"Content-Type": "application/x-www-form-urlencoded"}
    body = {
         "account": user,
        "password": psw,
        "referer": "http://192.168.0.138/zentao/bug-browse-13-0-unconfirmed-0.html",
    }

    r = s.post(url, headers= hear, data=body)
    print(r.status_code)
    print(r.text)
    return r.content.decode("utf-8")


if __name__ == '__main__':
    s = requests.session()
    loginRes = login(s, "caoyunpu", "3f68909318adc0fa5f18b3717e077380")
    result = is_login_sucess()
    print("测试登录结果：%s"%result)