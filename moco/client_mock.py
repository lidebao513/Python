#! /usr/bin/env python
#-*-coding:utf-8-*-
import requests
def send_xiaobao(url):
    r = requests.get(url)
    return r.status_code

def visit_xiaobao():
    return send_xiaobao('http://www.baidu.com')