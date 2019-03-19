#! /usr/bin/env python
#-*-coding:utf-8-*-

from selenium import webdriver
import unittest
class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

    def test_baidu_so_enabled(self):
        '''首页 百度搜索输入框可编辑'''
        so = self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(allTest())