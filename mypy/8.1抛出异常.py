# 使用 raise 可以让程序产证异常报错
# 单纯的使用 raise 是没有意义的，
# 一般情况下，我们对程序有个预期，当我们认为某些事情可能会导致程序不能正常运行时
# 便可以主动的引发一个异常来警告某些条件不满足，或者给出一些调整建议
# 如一个计算除法的方法，当检测到被除数为 0 时，可以主动的报错，提示使用者不要给某些参数传 0。
def some_method(something):
    if something == 'nothing':
        raise Exception("It must be something here")
    print("do something with " + something)
#end


some_method("1")


