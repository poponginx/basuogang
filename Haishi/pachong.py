import requests, json

page = 1
while page < 5400:
    url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureList'
    data = {
        'orgCode': None,
        'punishObjName': None,
        'currentPage': page
    }
    header = {
        'Host': 'cspur.msa.gov.cn',
        'Content-Length': '37',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureListPage2'
    }
    res = requests.post(url=url, data=data, headers=header)
    res = res.content.decode('utf-8')
    res = json.loads(res)
    # print(res[0]['list'])
    lis = res[0]['list']
    for i in lis:
        id = i['id']
        url = 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureShow'
        data = {
            'id': id,
        }
        header = {
        'Host': 'cspur.msa.gov.cn',
        'Content-Length': '37',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://cspur.msa.gov.cn/HsXzcfAppSm3/index/doubleDisclosureListPage2'
        }
        res = requests.post(url, data=data, headers=header)
        res = res.content.decode('utf-8')
        res = json.loads(res, encoding='utf-8')[0]
        print(res)
        # punishObjName = res['punishObjName']
        # illegalClause = res['illegalClause']
        # caseNo = res['caseNo']
        # punishResult = res['punishResult']
        # cardId = res['cardId']
        # punishReference = res['punishReference']
        # decisionDateText = res['decisionDateText']
        # orgName = res['orgName']
        # print(orgName)
    #     with open('E:/violationRecord.txt', 'a', encoding='utf-8') as f:
    #         f.write(
    #             '\n' + '被处罚人名称:' + punishObjName + '\n' + '处罚事由（案由）:' + illegalClause + '\n' + '处罚决定书文号:' + caseNo + '\n'
    #             + '处罚内容:' + punishResult + '\n' + '行政相对人（当事人）代码:' + cardId + '\n' + '处罚依据：' + punishReference +
    #             '\n' + '处罚决定日期:' + decisionDateText + '\n' + '处罚机关：' + orgName + '\n' + '\n')
    # print('第%s页完成' % page)
    # page += 1
