#! /usr/bin/env python
#-*-coding:utf-8-*-


'''
函数：函数是一段可以重复调用的代码 通过输入的参数 返回对应的返回值
名字绑定的机制 把实际参数的值与形式参数的值名称绑定到一起
1 函数调用的时候  实际参数的值和顺序与形式参数的顺序一一对应
2 当在函数调用的时候 制定了形式参数的实际参数 这个时候并不是一一对应的 而是根据制定的值来进行的

'''

# def add(a,b):
# #     print(a+b)
# #
# # # add(1,2)
# # # add(b=3,a=2)
# #
# # add('xiao','bao')


# def info(name,age,address,sex):
#     print(u"name:{0},age:{1},add:{2},sex:{3}".format(name,age,address,sex))
#
# info('xiaobao',18,'shanghai','man')
#
# def userInfo(userID):
#     '''登录成功后查看用户基本信息'''
#     pass
#
# def login(username='xiaobao',password='admin'):
#     if username == 'xiaobao' and password =='admin':
#         print('success')
#     else:
#         print('fail login')
#
# login()
# login('xiaobao','xiaobao')

# 形式参数在前 默认参数在后
# def name_age(name,age=19):
#     pass

'''
函数的返回值：
1 一个函数是有返回值的
2 当一个函数 没有return的生活  它的返回值是none
3 当一个函数return 的生活 它的返回值是return后面的内容

函数的返回值意义：函数/方法的返回值是为了给另外一个函数/方法一个请求的参数而已
'''
# def add(a,b):
#     c =a + b
#     return c
# print(add(2,3))
'''
接口测试：查看用户信息 实现步骤
1 发生post请求 login请求登录成功
2 登录成功后 返回token
3 带着这个token 查看用户信息
'''

def login(username='xiaobao',password='admin'):
    if username=='xiaobao'and password=='admin':
        return 'adasdsadasdasd'
    else:
        return 'login fail'
def userInfo(token):
    '''查看用户信息'''
    if token =='adasdsadasdasd':
        print(u'显示登录信息')
    else:
        print('loginout')

userInfo(login())