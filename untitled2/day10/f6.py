#!/usr/bin/env python
#-*-coding:utf-8-*-



import  unittest
from selenium import  webdriver

class F6(unittest.TestCase):
	def test_user_002(self):
		'''添加用户'''
		print('add')

	def test_user_002(self):
		'''删除用户'''
		print('del')

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(F6)
    unittest.TextTestRunner(verbosity=2).run(suite)
