# coding=utf-8
# 展开嵌套的序列
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

# isinstance(x, Iterable) 用来检查某个元素是否是可迭代的
# 额外的 isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外
# 防止将它们展开成单个字符
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)

# yield from 在生成器中调用其他生成器作为子例程的时候使用
