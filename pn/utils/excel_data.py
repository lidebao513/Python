#! /usr/bin/env python
#-*-coding:utf-8-*-
import xlrd



class ExcelVariablle:
    caseid=0
    url=2
    request_data=3
    expect=4
    result=5
def getCassID():
    return ExcelVariablle.caseid
def getURL():
    return ExcelVariablle.url
def get_request_data():
    return ExcelVariablle.request_data
def getExpect():
    return ExcelVariablle.expect
def getResult():
    return ExcelVariablle.result
def getHeadersValue():
    '''获取请求头'''
    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Cookie': 'WEBTJ-ID=20190315114547-1697f74ae1643-00aefcfb7abea-333b5602-2073600-1697f74ae195c5; _ga=GA1.2.1027905190.1552621548; _gid=GA1.2.1764898521.1552621548; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552621548; user_trace_token=20190315114549-d290d4b8-46d4-11e9-95d0-5254005c3644; LGSID=20190315114549-d290d686-46d4-11e9-95d0-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=; LGUID=20190315114549-d290d90a-46d4-11e9-95d0-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221697f74b9f60-05c0cdfc66a981-333b5602-2073600-1697f74b9f7244%22%2C%22%24device_id%22%3A%221697f74b9f60-05c0cdfc66a981-333b5602-2073600-1697f74b9f7244%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=187992b597eae28dcaba5c8bc6f03a6a3fc7b235fd1fa213; _putrc=E73819C854937798; JSESSIONID=ABAAABAAAGFABEF67F66DAF4A01387B212E0974B28DE87E; login=true; unick=%E6%9D%8E%E5%BE%B7%E5%AE%9D; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=187; gate_login_token=23d4ec3784a1706ecce3d85b30ab6efc60f469027f43a522; index_location_city=%E4%B8%8A%E6%B5%B7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552621564; LGRID=20190315114605-dc0c6431-46d4-11e9-95d0-5254005c3644; TG-TRACK-CODE=index_search; SEARCH_ID=61d6502bdc7341f88a372ffea5ba893b',
        'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput='}
    return headers