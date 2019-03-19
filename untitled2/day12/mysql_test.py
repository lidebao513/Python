#! /usr/bin/env python
#-*-coding:utf-8-*-

import pymysql

# 查询
# def connMysql():
#     try:
#         conn = pymysql.connect(
#             host='192.168.0.104',
#             user= 'root',
#             passwd='123456',
#             db='test'
#         )
#     except Exception as e:
#         return e.args
#     else:
#         cur =conn.cursor()
#         # sql = 'select *  from  user where id =%s '
#         # params=(1,)
#         # 单条语句查询
#         # cur.execute(sql,params)
#         # data = cur.fetchone()
#         # print(data)
#
#         cur.execute('select  *  from user')
#         data=cur.fetchall()
#         # for item in data:
#         #     print(item)
#         db = [item for item in data]
#         print(db)
#     finally:
#         cur.close()
#         conn.close()

# #插入
# def insertMysql():
#     try:
#         conn = pymysql.connect(
#             host='192.168.0.104',
#             user= 'root',
#             passwd='123456',
#             db='test'
#         )
#     except Exception as e:
#         return e.args
#     else:
#         cur = conn.cursor()
#         # 单条插入
#         # sql = 'insert into user values (%s,%s,%s)'
#         # params = (3,'xiaomaolv','shanghai')
#         # cur.execute(sql, params)
#         # conn.commit()
#
#
#         # 多条插入
#         sql = 'insert into user values (%s,%s,%s)'
#         params = [
#             (4, 'lihongyi', 'shanghai'),
#             (5, 'son', 'shanghai')
#         ]
#         cur.executemany(sql, params)
#         conn.commit()
#     finally:
#         cur.close()
#         conn.close()


#删除
def deleteMysql():
    try:
        conn = pymysql.connect(
            host='192.168.0.104',
            user= 'root',
            passwd='123456',
            db='test'
        )
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        sql = 'delete from user where id=%s'
        params = (5,)
        cur.execute(sql, params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

class MysqlHelper:
    def conn(self):
        con=pymysql.connect(
            host='192.168.0.104',
            user='root',
            passwd='123456',
            db='test'
        )
        return con
    def get_one(self,sql,params):
        cur=self.conn().cursor()
        data=cur.execute(sql,params)
        result=cur.fetchone()
        return result
def checkValid(username,password):
    opera=MysqlHelper()
    sql='select *  from login where username=%s and password=%s'
    params=(username,password)
    result=opera.get_one(sql=sql,params=params)
    return result

def info():
    username= input('请输入用户名:\n')
    password = input('请输入密码:\n')
    result = checkValid(username,password)
    if result:
        print('登录成功,昵称:{0}'.format(username))
    else:
        print('登录失败')
if __name__ == '__main__':
    info()