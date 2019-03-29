#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao

dict1 ={'name':'xiaobao','age':20,'address':'shanghai'}
# 判断key值是否存在
age =20
if dict1.has_key('age'):
    pass
if age in dict1.values():
	if age >18 :
		print(dict1['age'])
else:
	print('sorry')

# clear 全部清空
# dict1.clear()
# print(dict1)

# copy 复制
# dict2 = dict1.copy()
# print(dict2)

# pop删除指定的key对应的value值 并且打印出来
# print(dict1.pop('age'))
# print(dict1)
# 获取字典中key对应的具体value值
# print(dict1['age'])
# print(dict1.get('age'))
# 获取所以的key值
# for key in dict1.keys():
# 	print(key)
#获取所有的value值
# for value in dict1.values():
# 	print(value)
# 对字典循环
# for key,value in dict1.items():
# 	print(key,':',value)

# 字符串与列表之间的转换
# str1 = 'ADMINyadmin'
# # 字符串转换为列表
# list1 = str1.split('y')
# print(list1,type(list1))
#
# # 列表转换为字符串
# print('y'.join(list1))

# 列表和元组之间的转换
# list1 = [1,2,3,4,5]
# # 列表转换为元组
# tuple1 =tuple(list1)
# print(tuple1,type(tuple1))
#
# list2 = list(tuple1)
# print(list2,type(list2))
#
# # 字典与列表之间的转换
# list1 = dict1.items()
# print(list1)
# # 列表转换为字典
# dict2 = dict(enumerate(list1))
# print(dict2,type(dict2))
#

dict3 = {
    "code":200,
    "msg":"成功!",
    "data":{
        "yesterday":{
            "date":"26日星期二",
            "high":"高温 12℃",
            "fx":"东风",
            "low":"低温 7℃",
            "fl":"<![CDATA[<3级]]>",
            "type":"多云"
        },
        "city":"上海",
        # "aqi":null,
        "forecast":[
            {
                "date":"27日星期三",
                "high":"高温 11℃",
                "fengli":"<![CDATA[<3级]]>",
                "low":"低温 7℃",
                "fengxiang":"东北风",
                "type":"小雨"
            },
            {
                "date":"28日星期四",
                "high":"高温 11℃",
                "fengli":"<![CDATA[<3级]]>",
                "low":"低温 6℃",
                "fengxiang":"无持续风向",
                "type":"多云"
            },
            {
                "date":"1日星期五",
                "high":"高温 12℃",
                "fengli":"<![CDATA[<3级]]>",
                "low":"低温 7℃",
                "fengxiang":"西南风",
                "type":"小雨"
            },
            {
                "date":"2日星期六",
                "high":"高温 11℃",
                "fengli":"<![CDATA[<3级]]>",
                "low":"低温 7℃",
                "fengxiang":"西北风",
                "type":"大雨"
            },
            {
                "date":"3日星期天",
                "high":"高温 8℃",
                "fengli":"<![CDATA[<3级]]>",
                "low":"低温 5℃",
                "fengxiang":"西北风",
                "type":"小雨"
            }
        ],
        "ganmao":"相对于今天将会出现大幅度降温，空气湿度较大，易发生感冒，请注意适当增加衣服。",
        "wendu":"8"
    }
}
'''
https://www.apiopen.top/weatherApi?city=上海
测试的地址
数据基于json格式的字符串类型的数据
一个标准
1 业务状态码 code：200
2 消息 msg
3 数据 data

断言：
1 业务状态吗 dict3['code']
2 数据   (dict3['data']['forecast'][0]['high'])
3 HTTP协议状态码的断言
'''

# 获取今天的温度
print(dict3['data']['forecast'][0]['high'])