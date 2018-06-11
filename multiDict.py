# coding=utf-8
# 字典一键添加多个值
from collections import defaultdict
L = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('c', 5)]
d = defaultdict(list)
for key, value in L:
    d[key].append(value)
