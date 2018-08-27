# coding=utf-8
# 在多个对象执行相同的操作
# itertools.chain()用法
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
# 讨论：
# chain()比a + b的形式更加高效，会节省更多的内存
