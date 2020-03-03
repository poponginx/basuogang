#!/usr/bin/env python3
# coding:utf-8

'''
优化爬取海事处罚网站
'''
import requests, time, json, logging
from multiprocessing import Pool

class HaiShi(object):
    def __init__(self):
        '''
        公共变量
        :return:
        '''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Referer': 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureListPage%20?MenuCode2=201307038',
            'Cookie': 'insert_cookie=78968004; JSESSIONID=23WDvH7d04PXpe8FcKg_WTfK0NTGkS-SZPFSpg_fklUUXONQB1Bw!835213104'
        }
        self.url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureList'
        self.s = requests.Session()
    def get_page(self):
        '''
        获取爬取的页码数
        :return:
        '''
        nwe_data = {
            'orgCode': None,
            'punishObjName': None,
            'currentPage': '1'
        }
        try:
            page_response = self.s.post(self.url, data=nwe_data, headers=self.headers, timeout=5)
            page_response = json.loads(page_response.content.decode('utf-8'))
            total_page = page_response[0]['tatalCount']
            return total_page
            # print(total_page)
        except Exception as e:
            print('出现错误1，错误为:%s'%e)
            logging.exception(e)
            #出现错误进行递归操作
            self.get_page()

    def get_haishi(self, page):
        '''
        获取海事处罚内容
        :return:
        '''
        data = {
            'orgCode': None,
            'punishObjName': None,
            'currentPage': page
        }
        try:
            haishi_response = self.s.post(self.url, data=data, headers=self.headers, timeout=10)
            haishi_response = json.loads(haishi_response.content.decode('utf-8'))
            job_list = haishi_response[0]['list']
            for i in job_list:
                id = i['id']
                # print(id)
                url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureShow'
                data = {
                    'id': id
                }
                try:
                    save_response = self.s.post(url, data=data, headers=self.headers, timeout=10)
                    save_response = json.loads(save_response.content.decode('utf-8'))[0]
                    punishObjName = save_response['punishObjName']
                    caseReasonName = save_response['caseReasonName']
                    caseNo = save_response['caseNo']
                    punishResult = save_response['punishResult']
                    cardId = save_response['cardId']
                    illegalClause = save_response['illegalClause']
                    decisionDateText = save_response['decisionDateText']
                    orgName = save_response['orgName']

                    def tke():
                        with open('E:/lianxi-pytest.txt', 'a+', encoding='gb18030', errors='ignore') as fw:
                                fw.seek(0)
                                lines = fw.readlines()
                                if "处罚决定书文号:" + caseNo + "\n" in lines:
                                    print('已爬取过2，跳过')
                                    # continue
                                else:
                                    fw.write('\n' + '被处罚人名称:' + punishObjName + '\n' + '处罚事由（案由）:' + caseReasonName + '\n'
                                            + '处罚决定书文号:' + caseNo + '\n'+ '处罚内容:' + punishResult + '\n'
                                            + '行政相对人（当事人）代码:' + cardId + '\n' + '处罚依据：' + illegalClause +
                                        '\n' + '处罚决定日期:' + decisionDateText + '\n' + '处罚机关：' + orgName + '\n' + '\n')
                                    fw.close()

                    with open('E:/aaaa.txt', 'a+', encoding='gb18030', errors='ignore') as fa:
                        fa.seek(0)
                        lines = fa.readlines()
                        if "处罚决定书文号:" + caseNo + "\n" in lines:
                            print('已爬取过1，跳过')
                            # continue
                        else:
                            tke()
                except Exception as e:
                    logging.exception(e)
                    print('出现错误2，错误为:%s'%e)
                    print('等待10秒后重新对当前页进行爬取...')
                    time.sleep(10)
                    print('再次进行爬取')
                    self.get_haishi(page)
        except Exception as e:
            logging.exception(e)
            print('出现错误3，错误为：%s'%e)
            print('等待10秒后重新对当前页进行爬取...')
            time.sleep(10)
            print('再次进行爬取')
            self.get_haishi(page)
        print('第%s页保存成功'%page)

if __name__ == '__main__':
    h = HaiShi()
    ye = h.get_page()
    t = int(ye)+1
    p = Pool(5)
    for page in range(1, t):
        p.apply_async(h.get_haishi, args=(page,))
    p.close()
    p.join()























