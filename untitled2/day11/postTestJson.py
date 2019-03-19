#!/use/bin/env python
#coding:utf-8




import requests
import  json

data={"username":"","password":""}

headers={
	'Content-Type':'application/json;charset=UTF-8',
	'Parkingwang-Client-Source':'ParkingWangAPIClientWeb'
}

r=requests.post(
	url='http://116.62.132.145:9090/v5/login',
	json=data,
	headers=headers)

print(r.json())