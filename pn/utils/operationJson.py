#! /usr/bin/env python
#-*-coding:utf-8-*-

import json
from utils.public import *
from utils.operationExcel import *
class OperationJson:
    def __init__(self):
        self.excel=OperationExcel()

    def getReadJson(self):
        '''获取json文件的数据'''
        with open(data_dir(fileName='requestData.json'),'r',encoding='utf-8') as fp:
            data =json.load(fp)
            return data

    def getRequestsData(self,row):
        '''获取请求参数'''
        return json.dumps(self.getReadJson()[self.excel.get_request_data(row=row)])



opera=OperationJson()
print(opera.getRequestsData(2))