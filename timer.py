#!/usr/bin/ruby -w
# -*- coding : utf-8 -*-
# import time as t

# class MyTimer():
# 	def __init__(self):
# 		self.unit=["年","月","日","时","分","秒"]
# 		self.prompt="计时尚未开始"
# 		self.lasted=[]
# 		self.begin=0
# 		self.end=0

# 	def __str__(self):
# 		return self.prompt

# 	__repr__=__str__

# 	def __add__(self,other):
# 		prompt="总共运行了"
# 		result = []
# 		for index in range(6):
# 			result.append(self.lasted[index]-other.lasted[index])
# 			if result[index]:
# 				prompt+=(str(result[index])+self.unit[index])
# 		return prompt

# 	#开始计时
# 	def start(self):
# 		self.begin = t.localtime()
# 		self.prompt="请先调用stop（）停止计时"
# 		print("开始计时")

# 	#停止计时
# 	def stop(self):
# 		if not self.begin:
# 			print("请先调用start计时")
# 		else:
# 			self.end=t.localtime()
# 			self._calc()
# 			print("计时结束")

# 	#内部方法，计算运行时间
# 	def _calc(self):
# 		self.lasted=[]
# 		self.prompt="总共运行了"
# 		for index in range(6):
# 			self.lasted.append(self.end[index]-self.begin[index])
# 			if self.lasted[index]:
# 				self.prompt+=(str(self.lasted[index])+self.unit[index])
# 		#为下一轮初始化
# 		self.begin=0
# 		self.end=0


# t1=MyTimer()
# print(t1)
# t1.start()
# t.sleep(1)
# print(t1)
# t.sleep(1.99)
# t1.stop()
# print(t1)


import wheel.pep425tags as w


print(type(w.get_supported()))