#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mar 14, 2018


"""

from flask import Blueprint, request
from utils import *
from controller import batch_transactions_handler, BalanceAgent
main = Blueprint('account', __name__)


@main.route('/api/Agreement/Insert',methods=["POST"])
@mock_403
def crteat_test_Insert():
    data = request.get_data()
    print(data)
    new_heandlere =BalanceAgent("Insert",data=data)
    result = new_heandlere.do_work()
    return result

@main.route('/api/Agreement/UpdateAgreement',methods=["POST"])
@mock_500
def crteat_test_UpdateAgreement():
    data = request.get_data()
    print(data)
    new_heandlere =BalanceAgent("UpdateAgreement",data=data)
    result = new_heandlere.do_work()
    return result

@main.route('/api/Contract/AgreementByAgid',methods=["GET"])
@mock_404
def crteat_test_AgreementByAgid():
    data = request.get_data()
    print(data)
    new_heandlere =BalanceAgent("AgreementByAgid",data=data)
    result = new_heandlere.do_work()
    return result


#
# @main.route('/api/campus/getCampusListByArea',methods=["POST"])
# @mock_403
# def crteat_test_dev():
#     data = request.get_data()
#     print(data)
#     new_heandlere =BalanceAgent("getCampusListByArea",data=data)
#     result = new_heandlere.do_work()
#     return result
#
# @main.route('/payment/PaymentTradeService/CreatePaymentBillBatch', methods=["POST"])
# # 使用@mock_404标签后返回404的返回值
# @mock_500
# def create_payment_bill_batch():
#     data = request.get_data()
#     print(data)
#     new_handler = BalanceAgent("CreatePaymentBillBatch", data=data)
#     result = new_handler.do_work()
#     return result
#
#
# @main.route('/payment/PaymentTradeService/SubmitPaymentBillBatch', methods=["POST"])
# def submit_payment_bill_batch():
#     data = request.get_data()
#     new_handler = BalanceAgent("SubmitPaymentBillBatch", data=data)
#     result = new_handler.do_work()
#     return result
#
#
# @main.route('/payment/PaymentTradeService/QueryPaymentBillBatch',methods=["POST"])
# def query_payment_bill_batch():
#     data = request.get_data()
#     new_handler = BalanceAgent("QueryPaymentBillBatch", data=data)
#     result = new_handler.do_work()
#     return result
#
#
# @main.route('/payment/PaymentTradeService/CancelPaymentBillBatch', methods=["POST"])
# def cancel_payment_bill_batch():
#     data = request.get_data()
#     new_handler = BalanceAgent("CancelPaymentBillBatch", data=data)
#     result = new_handler.do_work()
#     return result
#
#
# @main.route('/v1/batchTransactions', methods=["POST"])
# def batch_transactions():
#     data = request.get_data()
#     result = batch_transactions_handler(data)
#     return result

