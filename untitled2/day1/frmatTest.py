#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao

name = 'xiaobao'
age =30
addres ='shanghai'


print('my name is %s ,age is %s come from %s'%(name,age,addres))
#format
print('my name is {0} ,age is {1} come from {2}'.format(name,age,addres))
# 不建议使用
print('my name is {:s}, age is {:d},come from {:s}'.format(name,age,addres))
#建议使用
print('my name is {name} , age is {age}, come from  {addres}'.format(name = name,age= age,addres=addres))