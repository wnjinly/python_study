# coding=utf-8
# 迭代器和生成器切片
# 使用itertools.islice()函数


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# c[10:20]
# Traceback (most recent call last):
#   File "D:\Project\python_study\iter_slice.py", line 11, in <module>
#     c[10:20]
# TypeError: 'generator' object is not subscriptable

import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

# 需要注意的是islice()会消耗掉传入迭代器中的数据
# 如果需要之后再次访问这个迭代器的话，需要将它里面的数据放入一个列表中	列
