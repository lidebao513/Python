#! /usr/bin/env python
#-*-coding:utf-8-*-
'''
try--expect的执行步骤：
1.try代码执行正常，就不会执行expect的代码
2.只有try代码执行异常,就会执行expect的代码
'''
def div(a,b):
    print(a/b)
# # div(1,0)
# try:
#     div(1,0)
# except ZeroDivisionError as e:
#     print(e.args)

# def f(*args,**kwargs):
#     return kwargs
# print(f('xiaobao'))
try:
    div(1,99.99)
except Exception as e:
    print(e.args)

'''
try--expect-- else --finalyy:
1.先执行try，如果执行通过，就执行else代码,最后执行finally
2.如果try执行失败,就直接执行执行finally
'''

