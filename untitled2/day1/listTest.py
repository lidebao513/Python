#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao

list1 = [1,2,9,7,2,9,7,3,4,6]

#print(dir(list1))
#
# # 'append', 'clear', 'copy', 'count', 'extend', 'index',
# # #'insert', 'pop', 'remove', 'reverse', 'sort'
#
# #把元素插入到第几位
# list1.insert(4,5)
# print(list1)
#
# #在列表中出现几次
# print(list1.count(3))
#
# #索引 index
# print(list1.index(3))
#
# #pop 删除，默认删除最后一位并且打印出来
# print(list1.pop())
#
# #remove 指定删除的元素
# list1.remove(2)
# print(list1)
#
# #reverse 反转
# list1.reverse()
# print(list1)
#
# #sort从小到大
# list1.sort()
# print(list1)

#
# '''extend列表的合并'''
# list2 = ['admin','xiaobao']
# list1.extend(list2)
# print(list1)
# print(list2)

'''dir在自动化测试中的应用'''
from selenium.webdriver.common.alert import Alert
print(dir(Alert))