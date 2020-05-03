# 1. 内置异常
#   Exception               几乎所有的异常类都是从它派生而来的
#   AttributeError          引用属性或给它赋值失败时引发
#   OSError                 操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
#   IndexError              使用序列中不存在的索引时引发，为 LookupError 的子类
#   KeyError                使用映射中不存在的键时引发，为 LookupError 的子类
#   NameError               找不到名称（变量）时引发
#   SyntaxError             代码不正确时引发
#   TypeError               将内置操作或函数用于类型不正确的对象时引发
#   ValueError              将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
#   ZeroDivisionError       在除法或求模运算的第二个参数为零时引发

# 2. 自定义异常
#   python 的内置异常如上，可以使用继承的方法自己定义异常，一般用不到，不再提供例子

# 3. except 关键字
#   3.1 多个 except 关键字
try:
    code
except OSError:
    xx
except AttributeError:
    xx

#   3.2 一个 except  捕获多个异常
try:
    code
except (OSError, AttributeError):
    xx
# end
