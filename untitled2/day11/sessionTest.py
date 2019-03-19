#! /usr/bin/env python
#-*-coding:utf-8-*-

'''session'''

import  requests

def getHeader():
    headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Content-Type':'application/x-www-form-urlencoded'}
    return headers
loginData={
        'email':'18621593513',
        'icode': '',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': 1,
        'captcha_type': 'web_login',
        'password': '70fb7d23b5455d518035f7078692cc9bfdc7af66184d916e5c49a1872bf47a36',
        'rkey': 'e1caf15d859d1ba14bc74b79f0ef8545',
        'f': 'http%253A%252F%252Fwww.renren.com%252F970011668'}
def login():
    # 对手sessions进行实例化
    s = requests.Session()
    r=s.post(
        url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019202122988',
        data=loginData,
        headers=getHeader())
    return s

def gotProfile():

    r=login().get('http://www.renren.com/970011668/profile')
    print(r.text)
gotProfile()