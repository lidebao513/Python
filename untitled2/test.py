#! /usr/bin/env python
#-*-coding:utf-8-*-

#author:xiaobao

import requests

# r = requests.get('https://api.github.com/events')
# print(r)

# r= requests.post('http://httpbin.org/post',data={'key':'value'})
# print(r.text)

# payload = {'key1':'value1','key2':'value2'}
# r = requests.get('http://httpbin.org/get',params=payload)
# print(r.text)


# class Employee:
# 	'所有员工的基类'
# 	empCount = 0
#
# 	def __init__(self, name, salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount += 1
#
# 	def displayCount(self):
# 		print("Total Employee %d" % Employee.empCount)
#
#
# 	def displayEmployee(self):
# 		print("Name : ", self.name, ", Salary: ", self.salary)
#
# e=Employee('xiaobao',18)
# e.displayCount()
# e.displayEmployee()


class Test:
	def prt(self):
		print(self)
		print(self.__class__)


t = Test()
t.prt()



