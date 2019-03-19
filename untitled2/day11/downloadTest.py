#!/usr/bin/env python 
#-*-coding:utf-8-*-

'''
响应体内容工作流：
默认情况下，当你进行网络请求后，响应体会立即被下载。你可以通过 stream 参数覆盖这个行为，推迟下载响应体直到访问
Response.content 属性：
r=requests.get(request_url,stream=True)
此时仅有响应头被下载下来了，连接保持打开状态，因此允许我们根据条件获取内容：
if int(r.headers['content-length])<TOO_Long:
    content=r.content
你可以进一步使用 Response.iter_content 和 Response.iter_lines 方法来控制工作流，或者以 Response.raw 从底
层 urllib3 的 urllib3.HTTPResponse <urllib3.response.HTTPResponse 读取未解码的相应体
如果你在请求中把 stream 设为 True，Requests 无法将连接释放回连接池，除非你 消耗了所有的数据，或者调用了
Response.close。 这样会带来连接效率低下的问题。如果你发现你在使用 stream=True 的同时还在部分读取请求的
body（或者完全没有读取 body），那么你就应该考虑使用 with 语句发送请求，这样可以保证请求一定会被关闭：
with 接口案例.get('http://httpbin.org/get',stream=True) as r:
   #再此处处理响应
'''


import  requests
import  shutil

def headers():
	headers={"Content-Type":"application/vnd.ms-excel; charset=utf8"}

def login():
	headers={
		'Content-Type':'application/json; charset=UTF-8',
		'Parkingwang-Client-Source':'ParkingWangAPIClientWeb'}
	data={"username":"999333","mall_id":11,"password":"91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203"}
	r=requests.post(url='http://180.62.132.145:9090/v4/login',
	                json=data,
	                headers=headers)
	return r.json()['data']['token']



def doanload_file(doanload_path):
	r=requests.get(
		url='http://180.97.80.42:9090/v4/download?per_page=10&type=&ex_type=&vpl=&page=1&stime=1522512000&etime=1523589565&memo1=&memo2=&memo3=&_=0.034775238593485414&token={0}&down=issue'.format(
			login()),
		headers=headers(), stream=True)
	if r.status_code==200:
		with open(doanload_path,'wb') as f:
			for chunk in r.iter_content(chunk_size=1024):
				f.write(chunk)
	return

def doanload_file_raw(doanload_path):
	r=requests.get(
		url='http://180.62.132.145:9090/v4/download?per_page=10&type=&ex_type=&vpl=&page=1&stime=1522512000&etime=1523589565&memo1=&memo2=&memo3=&_=0.034775238593485414&token={0}&down=issue'.format(
			login()),
		headers=headers(), stream=True)
	if r.status_code==200:
		with open(doanload_path,'wb') as f:
			r.raw.decode_content=True
			shutil.copyfileobj(r.raw,f)
	return

doanload_file_raw('c:/ecp.xlsx')







