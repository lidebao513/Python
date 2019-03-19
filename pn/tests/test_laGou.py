#! /usr/bin/env python
#-*-coding:utf-8-*-

import unittest
from base.method import Method,IsContent
from page.laGou import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsContent()
        self.excel=OperationExcel()
        self.operationJson =OperationJson()
    # def test_laGou_001(self):
    #     '''拉钩 测试翻页'''
    #     r=self.obj.post(1)
    #     print(r.text)
    #     print(r.url)
    def statusCode(self,r):
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['error_code'],0)

    def isContent(self,r,row):
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row,str2=r.text))

    def test_laGou_001(self):
        '''拉钩 测试翻页'''
        r=self.obj.post(row=1,data=self.operationJson.getRequestsData(1))
        # self.statusCode(r=r)
        # self.assertTrue(self.p.isContent(1,r.text))
        self.isContent(r=r,row=1)
        # print(self.p.isContent(row=1,str2=r.text))
        print(r.text)
        # print(r.url)
        self.excel.writeResult(1,'pass')


    def test_laGou_002(self):
        '''使用重新赋值的参数作为查询条件'''
        r=self.obj.post(row=1,data=setSo('性能测试'))
        '''把值取到写在文件中'''
        list1 = []
        for i in range(0, 15):
            positionId = r.json()['content']['positionResult']['result'][i]['positionId']
            list1.append(positionId)
        writePositionId(json.dumps(list1))
    def test_laGou_003(self):
        '''参数关联的方式'''
        for i in range(15):
            r = self.obj.get(url=getUrl()[i])
            self.assertTrue(self.p.isContent(2, r.text))
        pass
if __name__ == '__main__':
    unittest.main(verbosity=2)