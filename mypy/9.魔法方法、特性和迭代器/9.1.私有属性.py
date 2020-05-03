# 首先考虑一个问题：为什么对象的属性要设置成私有，而通过方法来设置和获取值
# 比如一个Human 类有一个name属性
# 既然可以 h.name = "Alice", n = h.name 这样来设置和获取属性的值，为什么还要创建 get_name 和 set_name 方法呢
# 下面来看一个例子
class Human:
    def __init__(self, name, birthyear):
        self.name = name
        self.birth = birthyear
        self.age = 2019 - birthyear
# 定义了一个类，人类，包含名称、出生年份和年龄三个属性
# 然后创建一个人，Alice，出生于1984年，然后打印名称和年龄都没有问题
h = Human("Alice", 1984)
print(h.age)
print(h.birth)
# 这时候如果要修改这个人的出生年份，那么这个对象的状态就有问题了
# 所以修改birth的时候需要同时修改年龄，那么对于这个类的说明就要加上这一特殊说明
# 试想这个类以后是发布给其他人再用，一个粗心的程序员没有看到说明，那么将导致错误的后果
h.birth = 1988
print(h.age)
print(h.birth)

# 所以为了防止由于错误的调用，导致对象数据完整性被破坏，就需要限制对对象属性的直接访问，改用存储方法
# 如该类，在存储方法中加入重新计算 age 的逻辑就能保证对象的age不会错误
class Human:
    
    def __init__(self, name, birthyear):
        self.name = name
        self.birth = birthyear
        self.age = 2019 - birthyear
    
    def set_birth(self, birthyear):
        self.birth = birthyear
        self.age = 2019 - birthyear
print("===========================================")
h = Human("Alice", 1984)
print(h.age)
print(h.birth)
# 此时使用设置方法来修改属性，就能避免异常的结果
h.set_birth(1988)
print(h.age)
print(h.birth)
# 但是尽管增加了设置方法，一些带有恶意的使用者仍然可能直接调用属性，导致错误结果
h.birth = 1984
print(h.age)
print(h.birth)
# 所以还要将属性设置为外部不可见，使用 __ 开头的属性就不能被外部调用
# 所以同时还要增加 访问方法
class Human:
    
    def __init__(self, name, birthyear):
        self.__name = name
        self.__birth = birthyear
        self.__age = 2019 - birthyear
    
    def set_birth(self, birthyear):
        self.__birth = birthyear
        self.__age = 2019 - birthyear

    def get_age(self):return self.__age
    def get_birth(self):return self.__birth

print("===========================================")
