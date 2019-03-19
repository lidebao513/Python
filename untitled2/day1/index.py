#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao
'''
str1 = "你好"
print(str1)

# 问题：uft-8如何传唤为gbk的编码
# 1 把utf-8解码成为uncideo编码 decode() 解码的时候带着编码是未解码钱的编码格式
# 2 把unciodeo编码成gbk encode()


#把utf-8解码为unicode
strUnicode=str1.encode('utf-8')
print(type(strUnicode))

#把unicode转换为gbk  把cuncide转换为str
strGbk = strUnicode.decode('gbk')
print(type(strGbk))
'''

from selenium import webdriver
#
# driver =webdriver.Firefox()
# driver.get('http://www.baidu.com')
# print(type(driver.title))
# print(driver.title)
# str1 = u'百度一下，你就知道'
# assert driver.title in str1
# driver.quit()

driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
str1=u'百度一下，你就知道'
print(driver.title)
assert  driver.title in str1
driver.quit()
