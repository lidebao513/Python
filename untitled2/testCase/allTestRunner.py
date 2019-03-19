#! /usr/bin/env python
#-*-coding:utf-8-*-

import unittest
import os
import  HTMLTestRunner
import  time
'''
#如果是Python2,一定要加如下的代码，如果不加，出现写中文的时候出现enicode error的错误信息
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
def allTests():
	suite=unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None)
	return suite

def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def run():
	fp=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'testReport.html')
	HTMLTestRunner.HTMLTestRunner(
		stream=open(fp,'wb'),
		title='自动化测试报告',
		description='自动化测试报告详细信息').run(allTests())

if __name__ == '__main__':
    run()