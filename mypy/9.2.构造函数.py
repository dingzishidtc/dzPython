# 构造函数的格式就是 __init__,这样的方法，在创建对象的时候会自动调用，
class A:
    def __init__(self): print("init A")
a = A()

# 如果方法有参数，创建对象时可以直接传入参数 python 会处理参数的传递
class A:
    def __init__(self, name, age): print("init A", name, age)
a = A("Alice", 1)

# 继承时，如果子类没有定义__init__,创建子对象时会自动调用父类的__init__
class A:
    def __init__(self): print("init A")
class B(A): pass
b = B()

# 如果子类定义了 init，则使用子类自己的__init__方法
class A:
    def __init__(self): print("init A")
class B(A):
    def __init__(self): print("init B")
b = B()

# 如果子类定义了 init，同时希望父类的init也能调用，可以在子类的init方法中使用 super().__init__
class A:
    def __init__(self): print("init A")
class B(A):
    def __init__(self): super().__init__;print("init B")
b = B()