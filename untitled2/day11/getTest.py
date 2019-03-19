#! /usr/bin/env python
#-*-coding:utf-8-*-

import requests

# https://movie.douban.com/subject_search?search_text=%E6%97%A0%E6%B6%AF&cat=1002
# r = requests.get(url='https://movie.douban.com/subject_search?search_text=%E6%97%A0%E6%B6%AF&cat=1002')

paydata = {'earch_text':'流浪地球','cat':1002}
r = requests.get(url='https://movie.douban.com/subject_search',params=paydata)
# r = requests.get(url='https://movie.douban.com/')
print(r.status_code)
# print(r.text)
print(r.url)

# print(r.status_code)
# print(r.text)
# print(r.content)
# print(r.content.decode('utf-8'))
# print(r.url)
# print(r.encoding)
# print(r.json())
# json返回字典类型    text返回为字符串类型

