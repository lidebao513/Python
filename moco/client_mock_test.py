#! /usr/bin/env python
#-*-coding:utf-8-*-
from client_mock import *
import unittest
from unittest import mock
class xiaobaotest(unittest.TestCase):
    def test_success_xiaobao(self):
        success_xiaobao=mock.Mock(return_value=200)
        send_xiaobao=success_xiaobao
        self.assertEqual(visit_xiaobao(),success_xiaobao())

if __name__ == '__main__':
    unittest.main()