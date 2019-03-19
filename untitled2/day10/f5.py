#! /usr/bin/env python
#-*-coding:utf-8-*-


import  unittest
from selenium import  webdriver

class BaiduTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		pass
		# cls.driver=webdriver.Chrome()
		# cls.driver.maximize_window()
		# cls.driver.implicitly_wait(30)
		# cls.driver.get('http://www.baidu.com')

	@classmethod
	def tearDownClass(cls):
		pass
		# cls.driver.quit()

	def test_baidu_news(self):
		print(1)
		# self.driver.find_element_by_link_text('新闻').click()
		# self.driver.back()

	def test_baidu_map(self):
		print(2)
		# self.driver.find_element_by_partial_link_text('图').click()
		# self.driver.back()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BaiduTest('test_baidu_news'))
    suite.addTest(BaiduTest('test_baidu_map'))
    unittest.TextTestRunner(verbosity=2).run(suite)
