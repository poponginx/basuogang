import requests


def spider_jd():
    '''爬取京东充气娃娃商品页'''
    url = "https://item.jd.com/1070129528.html"
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text[:500])
    except:
        print("爬取失败")

if __name__ == '__main__':
    spider_jd()