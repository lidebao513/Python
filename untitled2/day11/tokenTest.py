#! /usr/bin/env python
#-*-coding:utf-8-*-
import requests
data={
	"username": "6666666666",
	"password": "94475e8c44ddb6c773e6ccfcd7d0333a616fdbeb0411532c2c3cb31644a1e1c7"
}

headers={
	'Content-Type':'application/json;charset=UTF-8',
	'Parkingwang-Client-Source':'ParkingWangAPIClientWeb'}

def login():
	r=requests.post('http://116.62.132.145:9090/v5/login',json=data,headers=headers)
	return r.json()['data']['token']


def infoGet():
	r=requests.post(
		url='http://116.62.132.145:9090/v5/infoGet',
		json={'token':login()},
		headers=headers)
	print(r.text)

infoGet()