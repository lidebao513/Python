#! /usr/bin/env python
#-*-coding:utf-8-*-

import  unittest

class F1(unittest.TestCase):
	def setUp(self):
		print('我已经做好了准备工作')

	def tearDown(self):
		print('已处理')

	def test_001(self):
		# admin
		print('adminm')

	def test_002(self):
		print('test')

	def test_003(self):
		self.assertEqual(1,'1')

if __name__ == '__main__':
    unittest.main(verbosity=2)
