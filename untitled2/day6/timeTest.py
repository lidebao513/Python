#! /usr/bin/env python
#-*-coding:utf-8-*-


import time as t
# print(dir(t))

# 获取当前时间的时间错
# print(int(t.time()))

# 获取当前时间
nowtime1 = (t.strftime('%y-%m-%d %H:%M:%S',t.localtime()))
print(nowtime1)

# 休眠两秒
t.sleep(2)
nowtime2 = (t.strftime('%y-%m-%d %H:%M:%S',t.localtime()))
print(nowtime2)