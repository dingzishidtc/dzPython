# 迭代是遍历集合一种方式，如数组的迭代是访问数组的所有元素，Range的迭代是访问范围内的每个数字
#
# 能够完成迭代的对象成为迭代器，以数组的遍历来解释迭代器工作原理是：
#       迭代器位于元素i，表示迭代器状态为i
#       此时可以执行一些子定义的代码
#       将迭代器切换到下一个状态，状态 i + 1，迭代器位于 i+1
#       重复以上过程，直到下一个状态不存在（比如 i+1 等于数组的长度时），表示迭代完成
#
# 为了完成这项工作，迭代器至少要有一个 __next__方法，能够将迭代器切换到下一个状态
# 最常用的使用迭代器的过程就是 for i in arr 类的调用，python在for in 的 内部实现使用了迭代器
#
# python 迭代器相关的方法如下
#
# 被迭代的目标实现方法
#    __iter__   返回一个迭代器
#
# 迭代器实现方法
#    __next__   将迭代器切换到下一个状态
#   
# 可以定义一个子定义的类如 MyRange 使其可以用于 for in
class MyRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    #end

    def __next__(self):
        self.current += 1
        if self.current >= self.end:
            raise StopIteration
        return self.current

    def __iter__(self): return self

#end

r = MyRange(0, 5)

for i in r: print(i)

# 这个版本的实现是有问题的，问题在于被迭代的目标和迭代器使用了同一个类
# 这样的话，当第一次迭代后，该对象的迭代状态已经抵达了最终状态，
# 再一次迭代同一个对象时，迭代状态并未重置，因此迭代便立刻结束了
for i in r: print(i)

# 合理的版本如下
class MyRangeIte:
    def __init__(self, start, end):
        self.start = start
        self.end   = end
        self.current = start;
    #end

    def __next__(self):
        self.current += 1
        if self.current >= self.end:
            raise StopIteration
        return self.current
    #end

#end

class MyRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self): return MyRangeIte(self.start, self.end)

#end

print("=========================================")
r = MyRange(0, 5)

for i in r: print(i)
for i in r: print(i)









