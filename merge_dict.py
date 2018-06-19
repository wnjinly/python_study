# coding=utf-8

# 合并来个字典
# 使用collections.ChainMap(),可以保持原有俩个字典不变
# 只是在内部创建了一个内部容纳这些字典的列表

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c)
# 进行查找操作时，会先从a中查找，找不到才从b中查找
print(c['x'])
print(c['z'])
# 对于字典的大部分操作都可以进行
print(len(c))
print(list(c.keys()))
print(list(c.values()))
# 需要注意的是对于重复的键，第一次出现的映射会被返回
# 更新或删除操作总是作用于第一个字典


# 使用update()方法也可以将俩个字典合并，但它是创建一个新的字典
# 所有改变原有字典时，新的字典并不会收到影响

# ChainMap并不是创建一个新的字典，所有原有字典改变时，新的字典也会改变