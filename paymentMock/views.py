# -*- coding: utf-8 -*-
"""
Created on Mar 14, 2018

@author: guxiwen
"""

from flask import Blueprint, request
from utils import *
from controller import batch_transactions_handler, BalanceAgent
main = Blueprint('account', __name__)


@main.route('/payment/PaymentTradeService/CreatePaymentBillBatch', methods=["POST"])
@mock_404
def create_payment_bill_batch():
    data = request.get_data()
    print data
    new_handler = BalanceAgent("CreatePaymentBillBatch", data=data)
    result = new_handler.do_work()
    return result


@main.route('/payment/PaymentTradeService/SubmitPaymentBillBatch', methods=["POST"])
def submit_payment_bill_batch():
    data = request.get_data()
    new_handler = BalanceAgent("SubmitPaymentBillBatch", data=data)
    result = new_handler.do_work()
    return result


@main.route('/payment/PaymentTradeService/QueryPaymentBillBatch',methods=["POST"])
def query_payment_bill_batch():
    data = request.get_data()
    new_handler = BalanceAgent("QueryPaymentBillBatch", data=data)
    result = new_handler.do_work()
    return result


@main.route('/payment/PaymentTradeService/CancelPaymentBillBatch', methods=["POST"])
def cancel_payment_bill_batch():
    data = request.get_data()
    new_handler = BalanceAgent("CancelPaymentBillBatch", data=data)
    result = new_handler.do_work()
    return result


@main.route('/v1/batchTransactions', methods=["POST"])
def batch_transactions():
    data = request.get_data()
    result = batch_transactions_handler(data)
    return result

