#!/usr/bin/env python
#-*-coding:utf-8-*-

import  unittest
from untitled2.day10.init import *


def add(a,b):
	return a-b

class BaiduLink(Init):
	@unittest.skip('该功能已经取消，忽略该测试用例的执行')
	def test_baidu_news(self):
		self.driver.find_element_by_link_text('新闻').click()

	def test_002(self):
		self.driver.find_element_by_link_text('地图').click()

	@unittest.expectedFailure
	def test_003(self):
		self.assertEqual(add(3-2),1)


if __name__ == '__main__':
	unittest.main(verbosity=2)
