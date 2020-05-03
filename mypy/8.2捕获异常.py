# 语法
# try:
#   some_code_here
# except Exception:
#   do_something_after_exception
# #end
class Box:

    def __init__(self, name, remain):
        self.name   = name
        self.remain = remain
        self.stat   = "CLOSED"
    #end

    def open(self):
        self.stat = "OPENED"
        print(self.name, ": 打开")
    #end

    def close(self):
        self.stat = "CLOSED"
        print(self.name, ": 关闭")
    #end

    def pop(self):
        print(self.name, ": 取出一个物品")
        if self.remain == 0 :
            raise Exception(self.name + " is empty, cannot pop anything out")
        self.remain -= 1
    #end

    def put(self):
        print(self.name, ": 放入一个物品")
        self.remain += 1
    #end

#end

# 首先定义一个Box类，表示一个盒子，盒子里有若干个(remain)东西
# 盒子可以打开(open)，可以关闭(close)，可以取出(pop)，可以放入(put)
# 如果盒子中的物品数量为 0，则再取出的时候将会报错
#
# 用过一段程序模拟从 box1 拿 n 个东西，放到box2的过程如下
box1 = Box("box1", 3)
box2 = Box("box2", 0)
n = 2

box1.open()
box2.open()
for i in range(0, n):
    box1.pop()
    box2.put()
#end
box1.close()
box2.close()

# 上面这段程序的运行是没有问题的，问题是n的数量超过了box1的剩余数量
# 那么程序最后会报错，再这里报错并没有什么重要的后果，报错的结果是 close 方法的不到调用，那么box的stat将是 OPENED
# 试想如果 box 是一个数据库，是一个实际存在的仓库，等等
# 所以有必要确认在任何情况下 box 均能正常关闭，因此需要捕获异常

box1.open()
box2.open()
try:
    for i in range(0, n):
        box1.pop()
        box2.put()
    #end
except Exception:
    box1.close()
    box2.close()
box1.close()
box2.close()

# 这个时候会发现，如果发生了异常，最后close方法会被调用两次，因此需要将异常和非异常的路径区分开来
# 可以使用 else 关键字
box1.open()
box2.open()
try:
    for i in range(0, n):
        box1.pop()
        box2.put()
    #end
except Exception:
    # 异常时的操作
    box1.close()
    box2.close()
else:
    # 正常情况的操作
    box1.close()
    box2.close()

# 注意到关闭方法被写了两次，实际上，目标是无论是否发生异常都要调用close
# 因此可以使用finnaly

box1.open()
box2.open()
try:
    for i in range(0, n):
        box1.pop()
        box2.put()
    #end
except Exception:
    pass
else:
    pass
finally:
    # 最终操作
    box1.close()
    box2.close()
#end

# 实际上从功能的角度来说 try: finally 是没有必要的，如下代码的效果和使用 finally 的效果是一致的
# 但是 写在finally 中，显得更紧凑一点，因此实际代码中还是推荐 try finally 的形式
box1.open()
box2.open()
try:
    for i in range(0, n):
        box1.pop()
        box2.put()
    #end
except Exception:
    pass
# end

# 最终操作
box1.close()
box2.close()