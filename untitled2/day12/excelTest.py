#! /usr/bin/env python
#-*-coding:utf-8-*-

import xlrd
import os
from xlutils.copy import  copy
def base_dir(filename=None):
     return os.path.join(os.path.dirname(__file__),filename)

'''Excel的文件操作'''
# work = xlrd.open_workbook(base_dir('data.xls'))
# sheet = work.sheet_by_index(0)
# # 查看多少行
# print(sheet.nrows)
# #获取单元格的内容
# print(sheet.cell_value(4,1))

'''excel文件内容的修改'''
work = xlrd.open_workbook(base_dir('data.xls'))
old_content = copy(work)
ws = old_content.get_sheet(0)
ws.write(3,3,'小宝你好')
old_content.save(base_dir('data.xls'))

