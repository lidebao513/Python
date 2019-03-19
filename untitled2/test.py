#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao

import requests

# r = requests.get('https://api.github.com/events')
# print(r)

# r= requests.post('http://httpbin.org/post',data={'key':'value'})
# print(r.text)

payload = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=payload)
print(r.text)