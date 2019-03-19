#! /usr/bin/env python
#-*-coding:utf-8-*-
import csv
import requests
# def readCsvList():
#     with open('excel.csv','r') as f:
#         reader = csv.reader(f)
#         next(reader)
#         for item in reader:
#             print(list(item)[0])

def readCsvList():
    with open('excel.csv','r') as f:
        reader = csv.DictReader(f)
        # next(reader)
        for item in reader:
            print(dict(item)['测试用例'])

#
# url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
#
# def getHeaders():
#     headers={
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
#         'Cookie': 'GA1.2.59091575.1552221187; user_trace_token=20190310203306-a7e5100a-4330-11e9-90b4-5254005c3644; LGUID=20190310203306-a7e5195a-4330-11e9-90b4-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221696797da46ab4-02ce3f19bfd3e2-5d1e331c-1049088-1696797da472e1%22%2C%22%24device_id%22%3A%221696797da46ab4-02ce3f19bfd3e2-5d1e331c-1049088-1696797da472e1%22%7D; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=186; index_location_city=%E4%B8%8A%E6%B5%B7; WEBTJ-ID=20190312230104-169726bda5e43a-0238a36385ca9-5d1e331c-2073600-169726bda5fc53; _gid=GA1.2.1931964063.1552402865; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552221187,1552221196,1552402865,1552402874; LGSID=20190312230112-ad2965ee-44d7-11e9-bd14-525400f775ce; PRE_UTM=m_cf_cpc_baiduby_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.000000jk39biGWe9FEPP_YrUwj3nc99-pbbarpi_jUgNdvEa3FLtKXEPhxUC-QU4aUcXPuVtcG-lQxJvyfTCUkRLog-U5BHvDgL-8N2X-E9Pm9p-sTvQ4TmJSw1hiLMoDqc6ayQ4tSTVzq0j1qpOluLt301iVJsFgMu0TcAIjNG08m-G2uuq25C78kUcckIMSMHUsrhZYVarLkr8uf.DR_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsglrgZjdYtEUsng_3_7SW-9kst_IgQu8lISEG4xAkMGLU8gj4qrZul3IhOj4e_r1dsSEM9tOZjlOQjEosSxH9vX8Zxl3x5u9vN3ISkHReiM-kl-9h9molXPMmC0.U1Yk0ZDqs2v4VnL3FHcsdIjA80Kspynqn0KY5TaV8UHPSPgfko60pyYqnWcd0ATqmhNsT1D0Iybqmh7GuZR0TA-b5Hc0mv-b5Hfsr0KVIjYknjD4g1DsnHIxnW0vn-tknjc1g1nvnjD0pvbqn0KzIjYdnWm0uy-b5HDYn19xnWDknHIxnW6vnj9xnW6drjwxnW6dPH9xnW6vnjPxnW6vnjm0mhbqnW0Yg1DdPfKVm1Yknj0kg16kPH0zPH61ndtknj0dnjmkP1m3g17xn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5HD4P1bvnWmsn6K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyPV0ZwdT1YLnHDdnWR3Pj04njb4PHRsrj0k0ZF-TgfqnHRdnWfsnW6vnjTYPsK1pyfquAuWPANWm1nsnj0kmhRsmsKWTvYqwbwanDFKwRuAPDmdfbFjrfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10W0APzm1YYrHfLns%26word%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2B%25E6%258B%259B%25E8%2581%2598%26ck%3D7578.2.127.365.558.373.557.209%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.2.0.1.301.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baiduby_pc%26m_kw%3Dbaiduby_cpc_sh_0569f6_70a655_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%25E6%258B%259B%25E8%2581%2598; JSESSIONID=ABAAABAAAFCAAEGA5C3F11BB44C2EF45E418266BF118EAC; login=false; unick=""; _putrc=""; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=76d33960a956f1f8ede5968d12c39e52; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552403690; LGRID=20190312231448-934b26ac-44d9-11e9-bd23-525400f775ce; SEARCH_ID=5f8803d335594edcba6191afbfdb6cfe',
#         'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput='
#         }
#     return headers
# def laGou():
#     r= requests.post(
#         url=url,
#         headers=getHeaders(),
#         data={'first':'true','pn': 1,'kd':'自动化测试'}
#     )
#     print(r.text)
# laGou()

data = {'popFlag':'2','status':'done','_':'小宝'}
url='https://zhidao.baidu.com/task/api/getmytasklist'
def getHeaders():
    headers = {'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cookie': 'BAIDUID=BA04356BF9150246BC58DF88697E11D6:FG=1; BIDUPSID=BA04356BF9150246BC58DF88697E11D6; PSTM=1544337146; BDUSS=VJNZ0I5Z0Q1ME9vcHZycjc2M1NBeXk4MzFWLXJsdTlRREdDcHNnd09WRnMzb1JjQVFBQUFBJCQAAAAAAAAAAAEAAABqq8wLOTAzMzM0MzQzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGxRXVxsUV1ca; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=1438_21117_28608_28584_28558_28603_28606; BDSFRCVID=d88sJeCCxG3JFTQ97DFXjtAgNpRaCS_xAsmV3J; H_BDCLCKID_SF=JbAjoKK5tKvbfP0kh-QJhnQH-UnLqhoG257Z0lOnMp05OlQ20jubQMKVhPThQhvDLD6mbM7y04OVSCO_e6t5D5J0jN-s-bbfHDJK0b7aHJOoDDvge575y4LdLp7xJMTlQNC8_hbIyncMEJ38Kh5HLptm2-Qe2lKeWJQ2QJ8BJC82hDoP; ZD_ENTRY=baidu; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1551622891,1552140787,1552140876,1552222377; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1552222389; IKUT=8888',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
               'Referer': 'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=%D0%A1%B0%FC'
               }
    return headers
def test():
    r=requests.post(
        url=url,
        headers = getHeaders(),
        data=data
    )
    for i in range (5):
        positions=[]
        # print(r.json())
        uid = r.json()['data']['doing'][i]['uid']
        taskId = r.json()['data']['doing'][i]['taskId']
        taskStatus = r.json()['data']['doing'][i]['taskStatus']
        imgUrl = r.json()['data']['doing'][i]['imgUrl']
        gotoUrl = r.json()['data']['doing'][i]['gotoUrl']
        print(uid,taskId,taskStatus,imgUrl,gotoUrl)
        position={
            'uid': uid,
			'taskId': taskId,
			'taskStatus': taskStatus,
			'imgUrl': imgUrl,
			'gotoUrl': gotoUrl,
        }
        positions.append(position)

        for item in position:
            print(position)
        return item
def writeCsv():
	headers={'uid','taskId','taskStatus','imgUrl','gotoUrl'}
	positions=test()
        with open('111.csv', 'w') as f:
            writer=csv.DictWriter(f,headers)
            writer.writeheader()
            writer.writerows(positions)
writeCsv()