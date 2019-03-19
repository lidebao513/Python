#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao
'''
元组是不可变的 院子里面的元素数据是可变的
'''
tuple = (1,2,3,4,3,[1,2,3],{'name':'xiaobao'})

# # print(dir(tuple))
#'count', 'index'
'''count  元组中出现的次数'''
# print(tuple.count(3))
'''index 元素在元组中的索引'''
# print(tuple.index(4))

'''把元组中的列表【1，2，3】修改为【1，2，3，4】'''
# # print(tuple[5])
# tuple[5].insert(3,4)
# print(tuple)

'''把元组中的字典修改为 li'''
# print(tuple[6])
tuple[6]['name']='li'
print(tuple)
