import urllib.request
import urllib.parse
import time
import json
import hashlib

# content = input('请输入需要翻译的内容：')
'''
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
'''

# url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# data={}
# # data['i']=content
# data['i']='content'
# data['from']= 'AUTO'
# data['to']='AUTO'
# data['smartresult']= 'dict'
# data['client'] = 'fanyideskweb'
# data['salt']= int(time.time()*10000)
# data['sign'] = '92eef822f87d8b724a9cc6fa0133d942'
# data['ts'] = int(time.time()*1000)
# #bv参数是固定的
# data['bv'] = 'b396e111b686137a6ec711ea651ad37c'
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] = 'fanyi.web'
# data['action'] = 'FY_BY_REALTlME' 

# data=urllib.parse.urlencode(data).encode('utf-8')
# req = urllib.request.Request(url,data)
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
# rqpense = urllib.request.urlopen(req)

# html = rqpense.read().decode('utf-8')
# #此处获取到的html为字符型的就送文件，有两重处理方法
# # print(html)
# #处理方法1，将json字符类型转化为字典类型，然后通过下标定位
# aa=json.loads(html)
# # print(aa['translateResult'][0][0]['tgt'])
# result=aa['translateResult'][0][0]['tgt']
# print("翻译结果为:%s" %result)
# #处理方法2，直接用json.loads(html)的方式读取json文件，注：下面取出来的a是个字典类型，所以tgt还是得用字典的下标定位获取
# # a=json.loads(html)['translateResult'][0][0]
# # print(a)
# print(type(a))
# # print(a['tgt'])


#代理模式
# url="https://www.whatismyip.com.tw"
url = "http://www.fishc.com"
proxy_support=urllib.request.ProxyHandler({'http':'119.6.144.73:81'})
opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

rqpense = urllib.request.urlopen(url)
html=rqpense.read().decode("utf-8")

print(html)




# url = "http://www.fishc.com"
# url = "https://www.bilibili.com"
# url = 'http://placekitten.com/g/500/600'
# # req = urllib.request.Request(url)
# # rqpense=urllib.request.urlopen(req)
# # 上面2行等同于下面1行
# rqpense = urllib.request.urlopen(url)

# catimg = rqpense.read()
# with open('cat-500-600.jpg','wb') as f:
# 	f.write(catimg)
# # html=rqpense.read().decode("utf-8")
# # print(html)