# class Animal():
# 	"""docstring for Animal"""
# 	def __init__(self, name):
# 		super(Animal, self).__init__()
# 		self.name = name
# 	def eat(self):
# 		return self.name

# class Dog(Animal):
# 	"""docstring for Dog"""
# 	def __init__(self, name):
# 		super(Dog, self).__init__()
# 		self.name = name
# 	def eat(self):
# 		self.name="shiwu"
# 		return self.name
		

# a=Animal()
# b=Dog()
# A=a.eat("shiwu")
# B=b.eat('shi')
# print(A)
# print(B)
# # print(type(Animal.eat))
# # print(type(Dog.eat))

# class Ball:
# 	aaa="111"
# 	def setName(self,name,name1=2):
# 		self.name=name
# 	def kick(self):
# 		print (self.name)


# a=Ball()
# a.setName("qiuA3322",3)
# # b=Ball()
# # b.setName('qB')
# # c=Ball()
# # c.setName('qc')
# # print(a)
# # print(a.kick())
# print(a.aaa,'-----------------')


# class CapStr(str):
# 	def __new__(cls,string):
# 		string=string.upper()
# 		return str.__new__(cls,string)

# a=CapStr("asdasdasdsdfvczxfsdfsdf")
# print(a)


# class New_int(int):
# 	def __add__(self,intt):
# 		return int.__sub__(self,intt)

# a=New_int(1)
# b=New_int(2)
# print(a)
# print(type(b))
# c=int(1)
# print(type(c))
# print(a+b)


# class nonZero(int):
#     def __new__(cls,value):
#         # return int.__new__(cls,value) if value != 0 else None
#         return super().__new__(cls,value) if value != 0 else None
#     def __init__(self,skipped_value):
#         #此例中会跳过此方法
#         print("__init__()")
#         super().__init__()
# print(type(nonZero(-12)))
# print(nonZero(-12))
# print(type(nonZero(0)))
# print(nonZero(0))  
# 

#容器类
# class CountList:
list=['小明','小红','小蓝']
for item in enumerate(list):
	print(item)
# x = [i for i in range(5)]
# print(x)
print(__name__)


# #------------------------------------------------------------------------
#关于描述符的用法
# class MyProperty:
# 	def __init__(self,fget=None,fset=None,fdel=None):
# 		self.fget=fget
# 		print (self.fget,1111111)
# 		self.fset=fset
# 		print (self.fset,2222222)
# 		self.fdel=fdel
# 		print (self.fdel,3333333)

# 	def __get__(self,instance,owner):
# 		print("getting",self,instance,owner)
# 		return self.fget(instance)
# 		# 
# 	def __set__(self,instance,value):
# 		print("setting...",self,instance,value)
# 		return self.fset(instance,value)
# 	def __delete__(self,instance):
# 		# print("deleting...",self,instance)
# 		return self.fdel(instance)
# class C:
# 	m=1
# 	def __init__(self):
# 		self._x=MyProperty()
# 	def getX(self):
# 		return self._x
# 	def setX(self,value):
# 		self._x=value
# 	def delX(self):
# 		del self._x
# 	y=MyProperty(getX,setX,delX)
# c=C()
# # c.y="111"
# # print(c.y)
# c._x
# c.m
# # c.y


# class Desc(object):
# 	def __init__(self, name):
# 		self.name = name
# 		print("asdasdasdas")
	
# 	def __get__(self, instance, owner):
# 		print("__get__...")
# 		print('name = ',self.name) 
# 		print('='*40, "\n")

# class TestDesc(object):
# 	x = Desc('x')
# 	print("33333333333333333333333333333333333")
# 	def __init__(self):
# 		self.y = Desc('y')

# #以下为测试代码
# t = TestDesc()
# print("11111111111111111111111111111111111111111")
# print(t.y.__dict__)
# print("22222222222222222222222222222222222222222")
# t.x
# # t.x.__dict__

# class Desc(object):
#     def __init__(self, name):
#         self.name = name
#         print("__init__(): name = ",self.name)
        
#     def __get__(self, instance, owner):
#         print("__get__() ...")
#         return self.name

#     def __set__(self, instance, value):
#         self.value = value
        
# class TestDesc(object):
#     _x = Desc('x')
#     def __init__(self, x):
#         self._x = x
# class Celesius:
# 	def __init__(self,value=26.0):
# 		self.value=float(value)
# 	def __get__(self, instance, owner):
# 		print("__getcel__() ...")
# 		return self.value
# 	def __set__(self, instance, value):
# 		print("__setcel__() ...")
# 		self.value = float(value)
# class Fahrenheit:
# 	def __get__(self, instance, owner):
# 		print("__getfaf__() ...")
# 		return instance.cel*1.8+32
# 	def __set__(self, instance, value):
# 		print("__setfaf__() ...")
# 		instance.cel=(float(value)-32)/8
# class Temp:
# 	cel=Celesius()
# 	faf=Fahrenheit()

# temp=Temp()
# temp.cel
# print("2222222222")
# temp.faf=33
# print("1111111111")
# print(temp.cel)
# print("33333333333")
# print(temp.faf)


# #以下为测试代码
# t = TestDesc(10)
# t._x

# class Desc(object):
    
#     def __get__(self, instance, owner):
#         print("__get__...")
#         print("self : \t\t", self)
#         print("instance : \t", instance)
#         print("owner : \t", owner)
#         print('='*40, "\n")
        
#     def __set__(self, instance, value):
#         print('__set__...')
#         print("self : \t\t", self)
#         print("instance : \t", instance)
#         print("value : \t", value)
#         print('='*40, "\n")


# class TestDesc(object):
#     x = Desc()

# #以下为测试代码
# t = TestDesc()
# print(t.x)
# # print(TestDesc)
# # print(Desc)





# class C:
# 	def __init__(self):
# 		self._x = None
# 	@property
# 	def y(self):
# 		"""I'm the 'x' property."""
# 		return self._x
 
# 	@y.setter
# 	def y(self, value):
# 		self._x = value

# 	@y.deleter 
# 	def y(self):
# 		del self._x
# c=C()
# c.y="1"
# print(c.y)
# del c.y
# print(c.y)

# class Test(object):
# 	cls_val = 1
# 	def __init__(self):
# 		self.ins_val = 10
# t=Test()
# print(Test.__dict__)
# print(t.__dict__)
# t.cls_val=20
# print(t.__dict__)
# print(Test.__dict__)
# Test.cls_val=300
# print(t.__dict__)
# print(Test.__dict__)



# class MyDecriptor:
# 	def __get__(self,instance,owner):
# 		print("getting",self,instance,owner)
# 	def __set__(self,instance,value):
# 		print("setting...",self,instance,value)
# 	def __delete__(self,instance):
# 		print("deleting...",self,instance)
# class Test:
# 	x=MyDecriptor()
# 	a=1

# test=Test()
# print(test.x)
# test.x="111"
# del test.x


# #------------------------------------------------------------------------
# #关于配置类的属性
# class Cfx:
# 	def __init__(self,width=0,height=0):
# 		self.width=width
# 		self.height=height
# 	def __setattr__(self,name,value):
# 		if name=='square':
# 			self.width=value
# 			self.height=value
# 		else:
# 			# self.__dict__[name]=value
# 			super().__setattr__(name,value)
# 	def getArea(self):
# 		return self.width*self.height

# a=Cfx(4,5)
# a.square=10
# # print(a.width)
# # print(a.height)
# print(a.getArea())
# print(a.__dict__)


# class C:
# 	#用户访问存在的属性的时候执行__getattribute__内部操作
# 	def __getattribute__(self,name):
# 		print("getattribute")
# 		# return super().__getattribute__(name)
# 	#用户访问不存在的属性的时候执行__getsttr__内部操作
# 	def __getattr__(self,name):
# 		print("getattr")
# 	#用户设置类属性的时候执行__setattr__内部操作
# 	def __setattr__(self, name, value):
# 		print("setattr")
# 		super().__setattr__(name,value)
# 	#用户删除类属性的时候执行__delattr__内部操作
# 	def __delattr__(self,name):
# 		print("setattr")
# 		super().__delattr__(name)

# c=C()
# c.x




	# def __int__(self,size=10):
	# 	self.size = size
	# def getSize(self):
	# 	return self.size
	# def setSize(self,other):
	# 	self.size=other
	# def delSize(self):
	# 	del self.size
	# x=property(getSize,setSize,delSize)
# c = C()
# #c.x=1即通过x设置属性
# c.x=1
# print(c.size)
# #del c.x即通过x删除c的属性
# del c.x
# print(c.size)
  



