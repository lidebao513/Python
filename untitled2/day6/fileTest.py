#! /usr/bin/env python
#-*-coding:utf-8-*-

'''
open（）函数的参数
1 要操作的文件名称
2 以什么样的方式操作文件
r:只读模式
w:只写模式【不可读，不存在就创建，存在就清空内容】
x:只写模式【不可读，不存在就创建，存在就报错】
a:增加模式【可读，不存在就创建，存在只增加内容】
"+"表示可以同时读写某个文件，具体为：
r+：读写
w+：写读
x+：写读
a+：写读
'''
# f = open('file.json','w')
# temp = {
#     "name":"xiaobao",
#     "age":30,
#     "addres":"shanghai"
# }
# f.writelines(temp)
# f.close()
# 序列化的写入
# import json
# json.dump(temp,open('file.json','w'))
import json

'''追加'''
# f= open('file.json','a')
# f.write('xiaobao')
# f.close()

# 覆盖以前的内容 如果不存在则创建
# f= open('file.json','w')
# f.write('admin')
# f.close()

'''读文件 
read()  读取文件的所有内容
readlines() 默认读取文件第一行
read(7) 只读取文件中某些字符 
'''
# f = open('file1','r',encoding='utf-8')
# print(f.read())

# 默认读取文件第一行
# for i in f.readlines():
#     print(i)
#只读取前七个字
# print(f.read(7))

#
# f = open('file.json','r')
# print(f.read())


'''文件的上下文处理'''
# with open('file2','w') as f:
#     f.write('xiaobao')
#     不需要f.close()

with open('file2','r') as f:
    print(f.read())