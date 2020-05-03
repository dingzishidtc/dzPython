# 考虑一个定义严谨的类 Human，其中人的名字包括 姓氏 和 名字
# 当调用人的姓名方法时，应该返回 姓氏+名字
class Human:
    def __init__(self, familyName, givenName):
        self.familyName = familyName
        self.givenName = givenName

    def get_name(self):return self.familyName + " " + self.givenName

b = Human("李", "小红")
print(b.get_name())

# 函数 property 提供了一种快捷的可以为类增加 name 这种属性的方式
# 语法格式为：属性 = property(get方法, set方法)
# 这样 类在调用属性时就会自动调用get方法
# 类在给属性设置值时会自动的调用 set方法
class Human:
    def __init__(self, familyName, givenName):
        self.familyName = familyName
        self.givenName = givenName

    def get_name(self):return self.familyName + " " + self.givenName

    def set_name(self, name):
        self.familyName, self.givenName = name

    name = property(get_name, set_name)

#end

b = Human("李", "小红")
print(b.name)
b.name = ["张", "大红"];
print(b.name)

