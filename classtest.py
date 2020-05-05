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

class Ball:
	aaa="111"
	def setName(self,name,name1=2):
		self.name=name
	def kick(self):
		print (self.name)


a=Ball()
a.setName("qiuA3322",3)
# b=Ball()
# b.setName('qB')
# c=Ball()
# c.setName('qc')
# print(a)
# print(a.kick())
print(a.aaa,'-----------------')