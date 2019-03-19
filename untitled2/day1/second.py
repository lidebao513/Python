#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao
str1 ="ABCDef"
print('D在字符串的索引是第几位',str1.index('D'))
print('把字符串从小转为大写',str1.upper())
print('把字符串大写转为小写',str1.lower())
print('字符串是以A开始',str1.startswith('A'))
print('字符串以f结束',str1.endswith('f'))
# print('字符串转为列表',str1.split('D'))
print('字符串的替换',str1.replace('ef','EF'))
#实现字符串转为列表
print(str1.find('A'))
#实现列表转为字符串

'''
单引号和双引号的区别
1 在单引号中不能使用单引号
2 在双引号中不能使用双引号
3 在单引号中可以使用双引号
4 在双引号中可以使用单引号
'''
str2 = '"a"'
print(str2)
str3 = "'b'"
print(str3)
str4 = """c"""
print(str4)
str5 ="\"a\""
print(str5)