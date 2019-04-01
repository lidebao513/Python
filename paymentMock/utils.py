#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mar 14, 2018


"""
from functools import wraps
from flask import abort
from random import choice
import json
import requests
import time

# 封装post和get的方法

class Session(object):
    def __init__(self):
        self.session = requests.Session()
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}

    def post(self, url, params, json_data=None, headers=None):
        if headers is not None:
            self.headers = headers
        if json_data is not None:
            return self.session.post(url, json=json_data, headers=self.headers)
        return self.session.post(url, params, headers=self.headers)

    def get(self, url, params, headers=None):
        if headers is not None:
            self.headers = headers
        return self.session.get(url, params=params, headers=self.headers)

# 封装mock规则
class Mock(object):
    def __init__(self, mock_role):
        self.mock_role = mock_role

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 设置mock规则的statuscode
            if self.mock_role == "NotFound":
                abort(404)
            if self.mock_role == "ServerError":
                abort(500)
            if self.mock_role == "Forbidden":
                abort(403)
            if self.mock_role == "Timeout":
                # 支付系统默认超时时间10s
                time.sleep(12)
                abort(500)
            result = func(*args, **kwargs)
            result = json.loads(result)
            # 设置mock规则的返回值
            if self.mock_role == "allFail":
                result["Result"] = -1
            if self.mock_role == "partFail":
                fail_list = [21, 22, 23]
                result["Result"] = 0
                for detail in result["PaymentDetails"]:
                    detail["Status"] = 3
                result["PaymentDetails"][0]["Status"] = choice(fail_list)
            if self.mock_role == "Handling":
                handling_list = [0, 1, 2]
                result["Result"] = 0
                result["PaymentDetails"][0]["Status"] = choice(handling_list)
            if self.mock_role == "Success":
                success_list = [3, 11, 12, 13, 14, 15, 16, 19]
                result["Result"] = 0
                if result["PaymentDetails"]:
                    for detail in result["PaymentDetails"]:
                        detail["Status"] = choice(success_list)
            result = json.dumps(result)
            return result
        return wrapper


mock_404 = Mock("NotFound")
mock_403 = Mock("Forbidden")
mock_500 = Mock("ServerError")
mock_timeout = Mock("Timeout")
mock_all_fail = Mock("allFail")
mock_part_fail = Mock("partFail")
mock_handling = Mock("Handling")
mock_success = Mock("Success")
# 设置测试的ip地址或站点
APP_PREFIX = {"account": "http://172.18.18.98:9004", "balance": "http://zh-test.onesmart.org:810"}
# APP_PREFIX = {"account": "http://172.18.18.98:9004", "balance": "http://payment.trading.api.pay.ppdaicorp.com"}
TARGET_URL = {"batchTransactions": "http://172.18.18.98:9004/v1/batchTransactions",
              # 接口地址 调用需要 站点+URL
              "getCampusListByArea":"/api/campus/getCampusListByArea",
              "SubmitPaymentBillBatch": "/payment/PaymentTradeService/SubmitPaymentBillBatch",
              "CancelPaymentBillBatch": "/payment/PaymentTradeService/CancelPaymentBillBatch",
              "CreatePaymentBillBatch": "/payment/PaymentTradeService/CreatePaymentBillBatch",
              "QueryPaymentBillBatch": "/payment/PaymentTradeService/QueryPaymentBillBatch"}

# 解析json
def json_encode(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            result = json.dumps(result)
        except:
            pass
        finally:
            return result
    return wrapper