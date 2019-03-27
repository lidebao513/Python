#! /usr/bin/env python
#-*-coding:utf-8-*-
import requests
import shutil

def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit_baidu():
    return send_request('http://www.baidu.com')

class Remove(object):
    def rmdir(self,path='c/aaa'):
        r= shutil.rmtree(path)
        if r ==None:
            return 'success'
        else:
            return 'fail'

    def exists_get_rmdir(self):
        return self.rmdir()