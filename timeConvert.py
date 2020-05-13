import time as t
class timeConveny():
	def __int__():
		pass
# t1=t.localtime()
# t.sleep(2)
# t2=t.localtime()

# t1 = t.strptime("2020/05/09 22:12:32", "%Y/%m/%d %H:%M:%S")
# t3 = t.strptime("2022/06/19 23:11:02", "%Y/%m/%d %H:%M:%S")
# a=int(t.mktime(t1))
# b=int(t.mktime(t3))
# print(a)
# print(b)


# timeArray = t.gmtime(b-a)
# print(timeArray)
# print(b-a)
# # otherStyleTime = t.strftime("%Y年%m月%d天%H时%M分%S秒", timeArray)
# if b-a<60:
# 	otherStyleTime = t.strftime("%S秒", timeArray)
# elif b-a<60*60:
# 	otherStyleTime = t.strftime("%M分%S秒", timeArray)
# elif b-a<60*60*24:
# 	otherStyleTime = t.strftime("%H时%M分%S秒", timeArray)
# else:
# 	# otherStyleTime = t.strftime("%d天%H时%M分%S秒", timeArray)
# 	otherStyleTime = t.strftime("%Y年%m月%d天%H时%M分%S秒", timeArray)
# print(otherStyleTime)  

t1 = t.strptime("2020/05/09 21:12:32", "%Y/%m/%d %H:%M:%S")
t2 = t.strptime("3222/06/19 23:11:02", "%Y/%m/%d %H:%M:%S")

tt1=[]
tt2=[]
for i in range(6):
	tt1.append(t1[i])
	tt2.append(t2[i])
print(tt1)
print(tt2)

timeUnit=[60,24]
timeArray=[]
for i in range(6):
	if tt2[5-i]-tt1[5-i]<0:
		tt2[4-i]-=1 
		# timeArray.append(tt2[5-i]+timeUnit[i]-tt1[5-i])
		timeArray.append(str(tt2[5-i]+timeUnit[i]-tt1[5-i]))
	else:
		# timeArray.append(tt2[5-i]-tt1[5-i])
		timeArray.append(str(tt2[5-i]-tt1[5-i]))
# timeArray=timeArray[::-1]
# print(timeArray)
t2 = t.strptime("-".join(timeArray[::-1]), "%Y-%m-%d-%H-%M-%S")
print(t2)
t3 = t.strftime("%Y年%m月%d天%H时%M分%S秒", t2)
print(t3)

