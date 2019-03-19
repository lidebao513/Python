#! /usr/bin/env python
#-*-coding:utf-8-*-
import os

# print(os.system('ipconfig'))



# 创建个文件夹
#os.mkdir('c:/log')
# 删除文件夹
#os.rmdir(('c:/log'))

# 修改文件夹名称
# os.rename('c:/log','c:/newlog')

# 对目录的处理
# print(u'当前文件目录',os.path.dirname(__file__))
# print(u'当前文件上级目录',os.path.dirname(os.path.dirname(__file__)))



# 实现day3下login文件的内容读取
base_dir = os.path.dirname(os.path.dirname(__file__))

f = open(os.path.join(base_dir,'day3/login'),'r')

print(f.read())

