#! /usr/bin/env python
#-*-coding:utf-8-*-

import xml.dom.minidom
import os

def getXml(value=None):
    '''获取单节点的数据内容'''
    xmlFile = xml.dom.minidom.parse('data.xml')
    db=xmlFile.documentElement
    itemList=db.getElementsByTagName(value)
    item=itemList[0]
    return item.firstChild.data

print(getXml('yan'))
print(getXml('admin'))

# def getUser(parent=None,child=None):
#     '''获取单节点的数据内容'''
#     xmlFile = xml.dom.minidom.parse('data.xml')
#     db=xmlFile.documentElement
#     itemList=db.getElementsByTagName(parent)
#     item=itemList[0]
#     return item.getAttribute(child)
#
# print(getUser('Xiaobao','nick'))


def getUser(parent='Xiaobao',child=None):
    '''获取单节点的数据内容'''
    xmlFile = xml.dom.minidom.parse('data.xml')
    db=xmlFile.documentElement
    itemList=db.getElementsByTagName(parent)
    item=itemList[0]
    return item.getAttribute(child)

print(getUser(child='nick'))