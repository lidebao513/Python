#! /usr/bin/env python
#-*-coding:utf-8-*-


# def f1(name):
#     print(name)
#
# f1('xiaobao')

'''
*:arg  数据类型是元组
**kwargs 字典
'''
def f2(*args):
    print(args,type(args))
def f3( **kwargs):
    print( kwargs,type(kwargs))
def f4(name,age,sex,**kwargs):
    print(u'用户信息',name,age,sex,kwargs)
# f4('xiaobao',18,'man')
f4('xiaobao',18,'man',code ='asdasdsad',phone='262615654',addres='shanghai',work='test')
def f5(*args,**kwargs):
    print(args,kwargs)
f5()
f5(2)
f5('admin')
f5(['a','b'])
f5(address='shanghai')

