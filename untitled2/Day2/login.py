#! /usr/bin/env python
#-*-coding:utf-8-*-



'''
1 模拟登录
2 模拟登录成功显示登录成功后的账号
3 模拟注册
'''
def regetist(username,password):
    '''
    实现注册功能
    username:注册系统账号
    password：注册系统密码
    :return:
    '''
    temp = username+'|'+password
    f= open('login','w')
    f.write(temp)
    f.close()

def login(username,password):
    '''
    登录
    :param username: 登录系统的账号
    :param password: 登录系统的密码
    :return:
    '''
    f = open('login','r')
    for line in f :
        # print(line)
        # 把字符串转为列表
        list = line.split('|')
        # print(list)
        if list[0]==username and list[1]== password:
            # print(u'恭喜你登录成功')
            return True
        else:
            return False
    f.close()
def info(username,password):
    '''
    系统登录后成功的页面
    :return:
    '''
    f = open('login', 'r')
    for line in f:
        list = line.split('|')
    r= login(username,password)
    if r:
        print(u'恭喜{0}进入到系统'.format(list[0]))
    else :
        print(u'登录失败')
    f.close()
def exit():
    import sys
    sys.exit(1)

def typeUsername():
    username = input(u'请输入账号\n')
    return username
def typePassword():
    password = input(u'请输入密码\n')
    return password
def main():
    '''主函数'''
    while True:
        t = int(input('1、注册 2、 登录 3 退出登录\n'))
        if t ==1:
            username = typeUsername()
            password = typePassword()
            regetist(username,password)
        elif t ==2 :
            username = typeUsername()
            password = typePassword()
            login(username,password)
            info(username, password)
        elif t == 3:
            exit()
        else:
            print(u'输入错误请重新输入')
if __name__ == '__main__':
    main()