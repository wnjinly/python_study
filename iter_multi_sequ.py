# coding=utf-8
# 同时迭代多个序列
# 你想同时迭代多个序列，每次分别从一个序列中取一个元素。
# 使用zip()函数
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

# zip(a,b)生成一个可返回元组(x,y)的迭代器。一旦其中某个序列到结尾，迭代计数。
# 如果需要迭代出所有的元素，可以使用itertools.zip_longest()函数
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
# 此外，可以填充缺少的元素的值
for i in zip_longest(a, b, fillvalue=0):
    print(i)

# 扩展：zip()函数用途
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
# 打包生成字典
s = dict(zip(headers, values))
print(s)
# 自定义输出
for name, val in zip(headers, values):
    print(name, '=', val)
# 接受多于两个序列
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)
# zip()返回的是迭代器。要存储在列表中请使用list()函数
print(zip(a, b))
# <zip object at 0x1007001b8>
d = list(zip(a, b))
print(d)
