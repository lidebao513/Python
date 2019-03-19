#! /usr/bin/env python
#-*-coding:utf-8-*-



'''
1 模拟登录
2 模拟登录成功显示登录成功后的账号
3 模拟注册
'''
import json

#
# def regetist(username,password):
#     '''
#     实现注册功能
#     username:注册系统账号
#     password：注册系统密码
#     :return:
#     '''
#     temp = username+'|'+password
#     json.dump(temp,open('login','w'))
# def login(username,password):
#     '''
#     登录
#     :param username: 登录系统的账号
#     :param password: 登录系统的密码
#     :return:
#     '''
#     f = str(json.load(open('login', 'r')))
#     list1  = f.split('|')
#     if list1[0] == username and list1[1] == password:
#         return True
#     else:
#         return False
#
# def info(username,password):
#     '''
#     系统登录后成功的页面
#     :return:
#     '''
#     f = str(json.load(open('login', 'r')))
#     list1 = f.split('|')
#     r= login(username,password)
#     if r:
#         print(u'恭喜{0}进入到系统'.format(list1[0]))
#     else :
#         print(u'登录失败')
#     # f.close()
# def exit():
#     import sys
#     sys.exit(1)
#
# def typeUsername():
#     username = input(u'请输入账号\n')
#     return username
# def typePassword():
#     password = input(u'请输入密码\n')
#     return password
# def main():
#     '''主函数'''
#     while True:
#         t = int(input('1、注册 2、 登录 3 退出登录\n'))
#         if t ==1:
#             username = typeUsername()
#             password = typePassword()
#             regetist(username,password)
#         elif t ==2 :
#             username = typeUsername()
#             password = typePassword()
#             login(username,password)
#             info(username, password)
#         elif t == 3:
#             exit()
#         else:
#             print(u'输入错误请重新输入')
# if __name__ == '__main__':
#     main()
import sys


class Login(object):
    def __init__(self,usernmae,password):
        self.usernmae=usernmae
        self.password = password

    def getUsername(self):
        return self.usernmae

    def setUsername(self,username):
        self.usernmae=username

    def getPassword(self):
        return self.password

    def setUsername(self,password):
        self.usernmae=password

    def register(self):
        temp = self.usernmae + '|' + self.password
        json.dump(temp, open('login', 'w'))
        print(u'恭喜登录成功请登录')

    def login(self):
        f = str(json.load(open('login', 'r')))
        list1 = f.split('|')
        if list1[0] == self.usernmae and list1[1] == self.password:
            return True
        else:
            return False

    def info(self):
        f = str(json.load(open('login', 'r')))
        list1 = f.split('|')
        r = self.login()
        if r:
            print(u'恭喜{0}进入到系统'.format(list1[0]))
        else:
            print(u'登录失败')
    def exit(self):
        sys.exit(1)

def main():
    '''主函数'''
    per = Login('xiaobao','admin')
    while True:
        t = int(input('1、注册 2、 登录 3 退出登录\n'))
        if t == 1:
            per.register()
        elif t == 2:
            per.info()
        elif t == 3:
            per.exit()
        else:
            print(u'输入错误请重新输入')

if __name__ =='__main__':
    main()