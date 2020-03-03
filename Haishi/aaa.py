import time, json, requests
from multiprocessing import Pool

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureListPage2'
}
s = requests.Session()

def get_one_page():
    '''
    爬取页码数
    :return:
    '''
    one_url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureList'
    one_data = {
        'orgCode': None,
        'punishObjName': None,
        'currentPage': '1'
    }
    try:
        one_response = s.post(one_url, data=one_data, headers=headers, timeout=3)
        Transformation_response = json.loads(one_response.content.decode('UTF-8'))
        #取出总页数
        total_page = Transformation_response[0]['tatalCount']
        return total_page
    except Exception as mag:
        print('爬取页码数出现错误，错误为：%s'%mag)
        print('等待10秒后重新进行解析和获取')
        time.sleep(10)
        print('重新进行获取开始...........')
        get_one_page()

def get_new_page(page):
    '''
    爬取内容
    :return:
    '''
    two_data = {
        'orgCode': None,
        'punishObjName': None,
        'currentPage': page
    }
    new_url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureList'
    try:
        two_response = s.post(new_url, data=two_data, headers=headers, timeout=3)
        trans_response = json.loads(two_response.content.decode('UTF-8'))
        #提取爬取内容
        job_list = trans_response[0]['list']
        for i in job_list:
            id = i['id']
            two_url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureShow'
            three_data = {"id": id}
            three_response = s.post(two_url, data=three_data, headers=headers, timeout=3)
            #提取详情页的内容
            jobs_list = json.loads(three_response.content.decode('UTF-8'))[0]
            punishObjName = jobs_list['punishObjName']
            caseReasonName = jobs_list['caseReasonName']
            caseNo = jobs_list['caseNo']
            punishResult = jobs_list['punishResult']
            cardId = jobs_list['cardId']
            illegalClause = jobs_list['illegalClause']
            decisionDateText = jobs_list['decisionDateText']
            orgName = jobs_list['orgName']
            with open('F:/violationRecor.txt', 'a+', encoding='gb18030',   errors='ignore') as fa:
                fa.seek(0)
                lines = fa.readlines()
            with open('F:/violationRecor_20191225.txt', 'a+', encoding='gb18030',   errors='ignore') as fb:
                fb.seek(0)
                line = fb.readlines()
                if "处罚决定书文号:" + caseNo + "\n" in lines:
                    print('已爬取1，跳过')
                elif "处罚决定书文号:" + caseNo + "\n" in line:
                    print('已爬取2，跳过')
                else:
                    with open('F:/violationRecor_20191225.txt', 'a+', encoding='gb18030',   errors='ignore') as f:
                        f.write('\n' + '被处罚人名称:' + punishObjName + '\n' + '处罚事由（案由）:' + caseReasonName + '\n'
                                + '处罚决定书文号:' + caseNo + '\n'+ '处罚内容:' + punishResult + '\n'
                                + '行政相对人（当事人）代码:' + cardId + '\n' + '处罚依据：' + illegalClause +
                            '\n' + '处罚决定日期:' + decisionDateText + '\n' + '处罚机关：' + orgName + '\n' + '\n')
                        f.close()
    except Exception as mag:
        print('当前页爬取出现错误,错误为:%s'%mag)
        time.sleep(10)
        get_one_page()
    print('第%s页保存成功'%page)

if __name__ == '__main__':
    pages = get_one_page()
    total_page = int(pages)
    t = int(total_page)+1
    #设置5个进程跑
    p = Pool(5)
    #for循环提取页码数
    for page in range(1, t):
        p.apply_async(get_new_page, args=(page,))
    p.close()
    p.join()








