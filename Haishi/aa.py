import time, json, requests, urllib3, os, datetime
from multiprocessing import Pool
import datetime, os, shutil

urllib3.disable_warnings()
#公共变量
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureListPage2'
}
nowTime = datetime.datetime.now().strftime('%Y%m%d')  # 现在
url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureList'
s = requests.Session()#保持会话状态

def get_page_loca():
    '''
    取出上一次爬取的总页数
    :return:
    '''
    #读取本地上一次保存总页数的文件信息
    with open('E:/basuogang/pagelog/page.txt', 'a+', encoding='gb18030',   errors='ignore') as f:
        f.seek(0)
        lines = f.readlines()
        get_page = lines[0]
        return get_page

def get_new_page():
    '''
    爬取新的页码总数
    :return:
    '''

    new_data = {
        'orgCode': None,
        'punishObjName': None,
        'currentPage': '1'
    }
    try:
        new_response = s.post(url, data=new_data, headers=headers, timeout=10)
        new_response = json.loads(new_response.content.decode('utf-8'))
        #取出总页数
        total_page = new_response[0]['tatalCount']
        #将数据存入到文档中格式必须为字符串，然而获取到的数据为数字，所以需转换成字符串
        total_pages = str(total_page)
        #将新的总页数存放到文档中
        with open('E:/basuogang/page/page.txt', 'a+', encoding='gb18030',   errors='ignore') as f:
            f.write(total_pages)
            f.close()
        return total_page
    except Exception as mag:
        #出现错误进行捕捉，并使用递归函数进行重新对当页信息爬取
        print('出现爬取错误,错误信息是%s'%mag)
        get_new_page()

def get_total_page():
    '''
    获取到的新总页数减去上一次获取的总页数，new - loca
    :return:
    '''
    loca = get_page_loca()#获取到上一次的总页数
    new = get_new_page()#获取到新的总页数
    #对新，旧总页数进行转换成int类型
    loca = int(loca)
    new = int(new)
    try:
        total_page = new - loca#新，旧页数进行相减获取本次爬取的总页数
        ye = int(total_page)
        return ye
    except Exception as mag:
        print('出现新的总页数减去旧的总页数错误,重新进行两数相减，错误：%s'%mag)
        print('等待5秒后重新进行计算')
        time.sleep(5)
        print('开始重新计算')
        get_total_page()

def get_haishi(page):
    '''
    爬取海事内容
    :param page:
    :return:
    '''
    one_data = {
        'orgCode': None,
        'punishObjName': None,
        'currentPage': page
    }
    try:
        one_response = s.post(url, data=one_data, headers=headers, timeout=10)
        trans_response = json.loads(one_response.content.decode('utf-8'))
        #提取爬取内容
        job_list = trans_response[0]['list']
        for i in job_list:
            id = i['id']
            two_url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureShow'
            three_data = {"id": id}
            three_response = s.post(two_url, data=three_data, headers=headers, timeout=10)
            #提取详情页的内容
            jobs_list = json.loads(three_response.content.decode('utf-8'))[0]
            punishObjName = jobs_list['punishObjName']
            caseReasonName = jobs_list['caseReasonName']
            caseNo = jobs_list['caseNo']
            punishResult = jobs_list['punishResult']
            cardId = jobs_list['cardId']
            illegalClause = jobs_list['illegalClause']
            decisionDateText = jobs_list['decisionDateText']
            orgName = jobs_list['orgName']
            with open('E:/basuogang/violationRecor.txt', 'a+', encoding='gb18030',   errors='ignore') as f:
                f.seek(0)
                lines = f.readlines()
                if "处罚决定书文号:" + caseNo + "\n" in lines:
                    print('已爬取，跳过')
                    pass
                else:
                    with open('E:/basuogang/violationRecor.txt', 'a+', encoding='gb18030',   errors='ignore') as f:
                        f.write('\n' + '被处罚人名称:' + punishObjName + '\n' + '处罚事由（案由）:' + caseReasonName + '\n'
                                + '处罚决定书文号:' + caseNo + '\n'+ '处罚内容:' + punishResult + '\n'
                                + '行政相对人（当事人）代码:' + cardId + '\n' + '处罚依据：' + illegalClause +
                            '\n' + '处罚决定日期:' + decisionDateText + '\n' + '处罚机关：' + orgName + '\n' + '\n')
                        f.close()
    except Exception as mag:
        print('当前页爬取出现错误,错误信息为：%s'%mag)
        print('等待10秒后重新对当前页进行爬取...')
        time.sleep(10)
        print('再次进行爬取')
        get_haishi(page)
    print('第%s页保存成功'%page)

def totaltime():
    dir = "E:\\basuogang"
    try:
        for root, dirs, file in os.walk(dir):
            for b in file:
                if os.path.join(b).split('.')[1] == 'txt':
                    # os.rename(dir + os.sep + b, dir + os.sep + str(nowTime) + '_' + b)
                    shutil.move(os.path.join(dir, b),os.path.join("E:\\basuogang\\epsldplog", str(nowTime) + '_' + b))
    except Exception as mg:
        print('出现错误%s'%mg)

if __name__ == '__main__':
    ye = get_total_page()
    print('本次爬取新增了%s页内容'%ye)
    t = int(ye)+1
    p = Pool(5)
    #for循环提取页码数
    for page in range(1, t):
        p.apply_async(get_haishi, args=(page,))
    p.close()
    p.join()
    totaltime()