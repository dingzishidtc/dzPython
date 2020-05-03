# 前面介绍了 import sys 时，python 自己知道该去何地查询
# 那么有没有一种方式，能够在程序执行前让 python 知道该去何地查询，而不是每次都要调用 sys.path.append(xx)
#
# 这就要了解一下 python 查询模块的原理：
#   python 在导入模块时，是从 sys.path 保存的路径中依次查询指定模块是否存在，存在即导入。
#   因此可以通过修改sys.path 来增加 python 查询的路径，打印 sys.path 可以查看 python 的搜索范围 
#   一般来说 python 会从三个地方获取路径，然后存入 sys.path 中
#
#           1. 默认路径，以Python.3.7为例 大致有：
#                   ../Python37/python37.zip
#                   ../Python37/DLLs
#                   ../Python37/lib
#                   ../Python37/
#                   ../Python37/lib/site-packages
#           2. 当前程序路径
#           3. 环境变量 %PYTHONPATH% 中定义的路径
#   因此，对应的为了避免在程序中直接修改 sys.path 可以有三种方式
#           1. 将模块放入默认路径
#           2. 将模块放入当前程序路径
#           3. 将模块放入 环境变量 %PYTHONPATH% 中定义的路径 或 在 环境变量 %PYTHONPATH% 中加入模块路径
#
#   一般来说常用方式是，先在环境变量 %PYTHONPATH% 中加入指定的便于管理的路径，然后将模块都放入这些路径里。
#
#   对于之前的例子，可以先修改环境变量
#           C:\Users\rays1>echo %PYTHONPATH%
#           D:\environment\python\modules
#
#   然后将模块放入 D:\environment\python\modules
#
#   然后程序中就可以直接 import 模块
#
#   注意修改了环境变量后，要重新开启一个命令行或者重启IDE否则不会加载新的环境变量
import hero
import monster

h = hero.Hero()
m = monster.Monster()