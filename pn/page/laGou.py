#! /usr/bin/env python
#-*-coding:utf-8-*-
import json
from utils.public import *
from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel


operationJson=OperationJson()
def setSo(kd=None):
    '''对搜索的数据进行赋值'''
    dici1=json.loads(operationJson.get_RequestsData(1))
    print(dici1)
    dici1['kd']=kd
    return dici1
def writePositionId(content):
	'''把职位的ID写到文件中'''
	with open(data_dir(fileName='positionId'),'w') as f:
		f.write(content)
def getPositionId():
	'''获取职位招聘的信息'''
	with open(data_dir(fileName='positionId'),'r') as f:
		return json.loads(f.read())
def getUrl():
	listUrl=[]
	for item in getPositionId():
		url='https://www.lagou.com/jobs/{0}.html'.format(item)
		listUrl.append(url)
	return listUrl
