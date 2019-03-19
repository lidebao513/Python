#! /usr/bin/env python
#-*-coding:utf-8-*-
import requests

r= requests.get('http://www.baidu.com',timeout=6)
print(r.status_code)
# print(r.text)

r1=requests.get(url='https://www.12306.cn/mormhweb/',verify=False)
print(r1.content.decode('utf-8'))
#   忽略安全证书
