#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mar 15, 2018


"""
from utils import Session, APP_PREFIX, TARGET_URL
import json


def batch_transactions_handler(data):
    target_url = "http://172.18.18.98:9004/v1/batchTransactions"
    new_session = Session()
    result = new_session.post(target_url, data)
    return result.text


def submit_payment_bill_batch(data):
    target_url = ""
    new_session = Session()
    result = new_session.post(target_url, data)


class AgentBase(object):
    def __init__(self, app, func_name):
        self.new_session = Session()
        self.target_url = APP_PREFIX[app] + TARGET_URL[func_name]

    def do_work(self):
        raise NotImplementedError


class BalanceAgent(AgentBase):
    def __init__(self, func_name, method="POST", data=None):
        super(BalanceAgent, self).__init__("balance", func_name)
        self.method = method
        self.data = data

    def do_work(self):
        if self.method == "POST":
            print(self.data)
            result = self.new_session.post(self.target_url, self.data)
        else:
            result = self.new_session.get(self.target_url, self.data)
        print(result.text)
        return result.text
