import requests
#设置session会话变量
s = requests.session()


def douban():
    '''
    登录豆瓣电影
    user:18587977302
    password:caoyunpu110
    '''
    #请求的URL
    login_url = "https://accounts.douban.com/j/mobile/login/basic"
    #请求头部信息
    hear = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://accounts.douban.com/passport/login?source=movie",
            }
    #请求参数
    data = {
        "name": "18587977302",
        "password": "caoyunpu110",
        "remember": "false",
    }
    #加判断，如果为真就执行try，否则执行except
    try:
        #进行请求
        r = s.post(login_url, headers=hear, data=data)
        #查看状态
        r.raise_for_status()
        #打印出文本
        print(r.text)
    except:
        print("登录失败")


if __name__ == '__main__':
    douban()