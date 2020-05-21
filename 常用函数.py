#!/usr/bin/python 
# -*- coding : utf-8 -*-

# def findarr(arrold, a,hash1={}):
# 	b=hash1.get('num',0)
# 	arr1=arrold[0:int(len(arrold)/2)]
# 	arr2=arrold[int(len(arrold)/2):int(len(arrold))]
# 	print(hash1,arrold)
# 	if a in arr1:
# 		if int(len(arr1))==1:
# 			print(hash1['num'])
# 		else:
# 			findarr(arr1, a)
# 	elif a in arr2:
# 		hash1['num']=b
# 		hash1['num']+=int(len(arrold)/2)
# 		if int(len(arr2)==1):
# 			print(hash1['num'])
# 		else:
# 			findarr(arr2, a)
# 			print(hash1['num'])

# a=[1,2,3,4,5,6,7,8,9,10,22]
# findarr(a,10)

from suds.client import Client

header={}

user_url="http://localhost:8880/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl" #这里是你的webservice访问地址
client=Client(user_url)#Client里面直接放访问的URL，可以生成一个webservice对象
print(client)#打印所webservice里面的所有接口方法名称，结果如下截图所示：

#md5加密
# import time
# import hashlib

# #时间戳转化
# print(int(time.time()*10000))

# # 中文加密方法
# data="哈哈"
# str1_md5=hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
# #英文加密方法
# str2_md5 = hashlib.md5(b'18').hexdigest()
# print(str1_md5)
# print(str2_md5)


# print(len("92eef822f87d8b724a9cc6fa0133d942"))


# import classtest as A

# a=A.Ball()
# a.aaa="5555"
# a.setName("qiuA11",3)
# print(a.kick())
# print(a.aaa)



#---------------------------------------------------------------------------
# import easygui
# easygui.msgbox('Hello World')


#---------------------------------------------------------------------------
# import os
# # #显示当前目录
# # print(os.getcwd())
# # #修改当前目录
# # print(os.chdir("E:\\test"))
# # print(os.getcwd())
# # print(os.listdir())
# #发送到cmd窗口
# # os.system('cmd')
# # os.system('calc')
# #查看文件的时间属性
# import time
# #返回的时间格式，gmtime是国际时间，localtime是当地时间,
# #getatime是最近访问时间,getctime是创建时间，getmtime是修改时间
# a=time.gmtime(os.path.getatime('D:\\Users\\1.txt'))
# a=time.localtime(os.path.getatime('D:\\Users\\1.txt'))
# a=time.localtime(os.path.getctime('D:\\Users\\1.txt'))
# print(a)




#---------------------------------------------------------------------------
# #字典的批量赋值，fromkeys方法会直接创建一个新的字典
# dict1={444:"3333"}
# # print(dict1.fromkeys((1,2,3)))
# a=dict1.fromkeys((1,2,3),"2222")
# a=dict1.fromkeys(range(1,6),"2222")
# print(a)





#---------------------------------------------------------------------------
#sorted是用于对一个可迭代对象进行排序处理，排序依据是key的返回值

# sorted([1,-2,0,5],key=abs)
# print(sorted([1,-2,0,5],key=abs))
# example_list = [5, 0, 6, 1, 2, 7, 3, 4]
# result_list = sorted(example_list, key=lambda x: -x)
# result_list = sorted(example_list, key=lambda x: x*-1)
# print(result_list)
# result_list = map(lambda x: x*-1,example_list)
# print(list(result_list))
# result_list = sorted(example_list, key=abs)
# print(result_list)
# result_list = sorted(example_list, reverse=True)
# result_list = sorted(example_list)
# print(result_list)

# sorted升阶用法：先按照成绩降序排序，相同成绩的按照名字升序排序：
# d1 = [{'name':'alice', 'score':38}, {'name':'bob', 'score':18}, {'name':'darl', 'score':28}, {'name':'christ', 'score':28}]
# l = sorted(d1, key=lambda x:(-x['score'], x['name']))
# print(l)


#--------------------------------------------------------------------------
# map用于对一个数列中所有数据进击迭代处理，再返回一个数列


# import math
# def is_odd(n):
# 	return n % 2 == 1

# a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
# 	print(is_odd(i),i)
# print(list(filter(lambda x : math.sqrt(x) % 1==0,range(10))))

# print(list(filter(lambda x : x % 2,range(10))))

# print(list(filter(lambda x : x % 2,range(10))))


# print(list(map(lambda x : x % 2,range(10))))
# print(type(lambda x : x * 2,1))


# def f(s,b):
#     return s[0:1].upper() + s[1:].lower(),b[0:1].upper() + b[1:].lower()


# list1 = ['lll', 'lKK', 'wXy',"eeee"]
# list2 = ['www', 'qqqq', 'asSS',"eeee"]

# a = map(f, list1,list2)

# print(a)
# print(list(a))


#--------------------------------------------------------------------------
# 一个有趣的模块
# import turtle
# t=turtle.Pen()
# for x in range(90):
# 	t.forward(x)
# 	t.right(90)

# import sys
# sys.setrecursionlimit(100)