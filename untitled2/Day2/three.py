#! /usr/bin/env python
#-*-coding:utf-8-*-
'''
全局变量和局部变量
全局变量和局部变量同时存在的时候 选择局部变量
'''

# 全局变量
name ='xiaobao'
def f1():

    # 对全局变量进行一个修正
    global name
    name ='li'
    print(name)
f1()
# def f2():
#     # 局部变量
#     name='admin'
#     print(name)
# f2()