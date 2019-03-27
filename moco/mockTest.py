#! /usr/bin/env python
#-*-coding:utf-8-*-
import client
import unittest
from unittest import mock

class MockTest(unittest.TestCase):
    def setUp(self):
        self.r=client.Remove()
    def test_fail_send(self):
        fail_send=mock.Mock(return_value=404)
        client.send_request=fail_send
        self.assertEqual(client.visit_baidu(),404)
    def test_success_send(self):
        success_send =mock.Mock(return_value=200)
        client.send_request=success_send
        self.assertEqual(client.visit_baidu(),200)
    def test_remove_success(self):
        remove_success=mock.Mock(return_value='success')
        self.r.rmdir=remove_success
        self.assertEqual(self.r.exists_get_rmdir(),'success')
    def test_remove_fail(self):
        remove_fail=mock.Mock(return_value='fail')
        self.r.rmdir=remove_fail
        self.assertEqual(self.r.exists_get_rmdir(),'fail')
if __name__ == '__main__':
    unittest.main(verbosity=2)