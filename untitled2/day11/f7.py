#!/use/bin/env python
#coding:utf-8

# 认证

import  requests
# from  requests.auth import HTTPBasicAuth

r=requests.get('http://localhost:5000/hotel/username/',
               auth=('wuya','admin'))
print(r.text)