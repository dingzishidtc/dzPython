# 包即 package, 模块即 module,
# 可以这样简单的理解，module 是文件，package 是文件夹
# package 包含 module，package 也可以包含 package
#
# 当然还要做一些前期的工作，文件夹需要增加 __init__.py 才会被 python 解析为 pakage (实际测试的时候发现可以没有，可能是版本的关系，建议还是添加)
# __init__.py 中的代码将是包的内容，如可以在其中定义变量、方法等
#
# 如一个目录结构如下，环境变量定义为 D:\environment\python\modules
#
# D:\environment\python\modules
#  └─fakeGame
#     ├─ item
#     |   └─ sword.py
#     ├─ hero.py
#     └─ monster.py
from fakeGame import hero, monster
import fakeGame.items.sword

h = fakeGame.hero.Hero()
m = fakeGame.monster.Monster()
s = fakeGame.items.sword.Sword()
print("=================================================")

# 实际使用时会发现，在使用一个包下的任意一个模块时，都要显式引用模块，当一个包中包含了大量模块时，这种引用几乎是不可能的
# 考虑到在引入包时，会先调用 __init__.py ，因此可以借助 __init__.py 来实现包内部的自我引用
#
# 在 fakeGame2/__init__.py 中加入
#       import fakeGame2.items
#       import fakeGame2.hero
#       import fakeGame2.monster
#
# 在 fakeGame2/items/__init__.py 中加入
#       import fakeGame2.items.sword
#
# 那么在引入 fakeGame2 时，会先调用 fakeGame2/__init__.py，之后引用 import fakeGame2.items 会调用 fakeGame2/items/__init__.py
# 顺次下去，最终结果时 只要引入了 fakeGame2 这个包，包下面的所有模块都加载了
#
# D:\environment\python\modules
#  └─fakeGame2
#     ├─ __init__.py
#     ├─ item
#     |   ├─ __init__.py
#     |   └─ sword.py
#     ├─ hero.py
#     └─ monster.py
#
import fakeGame2

h = fakeGame2.hero.Hero()
h = fakeGame2.monster.Monster()
h = fakeGame2.items.sword.Sword()

# 这样就解决了大部分的问题，当然关于包的知识还有很多，这里不再具体介绍，遇到的时候再说把