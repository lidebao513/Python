#! /usr/bin/env python
#-*-coding:utf-8-*-

import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson


operationExcel=OperationExcel()


def checkHeader(row,f1=None,f2=None):
	'''检测请求头'''
	url=operationExcel.getUrl(row=row)
	url=url.split('/')
	if url[4]=='positionAjax.json?needAddtionalResult=false':
		return f1
	elif url[5]=='byPosition.json':
		return f2


class Method:
    def __init__(self):
        self.oprationJson=OperationJson()
        self.excel=OperationExcel()
    # def post(self,row):
    #     try:
    #         r=requests.post(
    #             url=self.excel.getUrl(row=row),
    #             data=self.oprationJson.get_RequestData(row=row),
    #             # data={'city':'上海','key':'0e3f87aa3f8238f52731a74d3a29e4eb'},
    #             headers=getHeadersValue(),
    #             timeout=6
    #         )
    #         return r
    #     except Exception as e:
    #         raise RuntimeError('接口请求发生未知异常')

    # def post(self, row):
    #     try:
    #         r = requests.post(
    #             url=self.excel.getUrl(row=row),
    #             # data=self.oprationJson.get_RequestData(row=row),
    #             data={'city': '上海', 'key': '0e3f87aa3f8238f52731a74d3a29e4eb'},
    #             # headers=getHeadersValue(),
    #             timeout=6
    #         )
    #         return r
    #     except Exception as e:
    #         raise RuntimeError('接口请求发生未知异常')

    def post(self,row, data):
        try:
            r = requests.post(
                url=self.excel.getUrl(row=row),
                # data=self.oprationJson.get_RequestData(row=row),
                data=data,
                # headers=getHeadersValue(),
                timeout=6
            )
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知异常')

    def get(self, url, params=None):
        r = requests.get(url=url, params=params, headers=getHeadersValue(), timeout=6)
        return r

class IsContent:
    def __init__(self):
        self.excel=OperationExcel()

    def isContent(self,row,str2):
        flag=None
        if self.excel.getExpect(row=row) in str2:
            flag=True
        else:
            flag=False
        return  flag