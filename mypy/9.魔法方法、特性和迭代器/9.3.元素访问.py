# 序列、字典在访问元素和设置值时，可以快捷的使用 arr[i] = xx, a = arr[i]
# 这种操作，背后也是python通过特殊的方法在支撑
# 自定义的一些类也可以通过定义特殊方法来使用快捷操作：
#   1. 通过 []     来访问元素，可以使用 __getitem__(self, key) 方法
#   2. 通过 []=    来设置元素，可以使用 __setitem__(self, key, value) 方法
#   3. 通过 del [] 来删除元素，可以使用 __delitem__(self, key) 方法
#   4. 通过 len(xx)来得到数量，可以使用 __len__(self) 方法
class PersonalStruct:
    def __getitem__(self, key):
        print("get", key)

    def __setitem__(self, key, value):
        print("set",key,"=",value)

arr = PersonalStruct()
arr[1]
arr[2] = 123