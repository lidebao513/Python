#! /usr/bin/env python
#-*-coding:utf-8-*-
import requests
import json

'''
序列化:把Python的数据类型转为字符串的类型过程
反序列化 把字符串的类型转为Python的数据结果
'''

# r=requests.post(url='https://ecapi.parkingwang.com/v5/login',
#                 headers={'Parkingwang-Client-Source':'ParkingWangAPIClientWeb',
#                          'Content-Type':'application/json;charset=UTF-8'},
#                 data=json.dumps({"username":"","password":""}))
# print(str(r.text))
# print(type(str(r.text)))
# print(json.loads(str(r.text))['msg'])

'''文件的序列化和反序列化'''
r = requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')
# print(r.content.decode('utf-8'))
# 对文件进行序列化 把服务器的相应文件写道文件中

json.dump(str(r.content.decode('utf-8')),open('weather.json','w'))
# 对文件的反序列化 读取文件的内容
dict1 = json.loads((json.load(open('weather.json','r'))).encode('utf-8'))

'''
1 文件反序列化后 类型是 unicode类型
2 进行编码 把Unicode类型转化为字符串 str类型
3 然后用反序列化把str转为字典类型
'''
# print(dict1)
# print(dict1,type(dict1))
print(dict1['weatherinfo']['city'])

# # 序列化 字典转为字符串
# dict1 = {'name':'xiaobao','age':18}
# dist_str = json.dumps(dict1)
# print(dist_str,type(dist_str))
#
# # 反序列化 把字符串转为字典
# str_dict = json.loads(dist_str)
# print(str_dict,type(str_dict))

# '''列表的序列号与反序列化过程'''
# list1 =['admin','xiaobao','hello']
# # 序列号
# list_str = json.dumps(list1)
# print(u'序列化后的结果',list_str,type(list_str))
#
# # 反序列化
# str_list = json.loads(list_str)
# print(u'反序列化后的结果',list_str,type(str_list))

'''元祖的序列号与反序列化的过程'''
# tuple1 = ('a','b','c')
# tuple_str = json.dumps(tuple1)
# print(u'序列化后的结果',tuple_str,type(tuple_str))
#
# str_tuple = json.loads(tuple_str)
# print(u'序列化后的结果',str_tuple,type(str_tuple))
