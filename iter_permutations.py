# coding=utf-8
# 你想迭代遍历一个集合中元素的所有可能的排列或组合
items = ['a', 'b', 'c']
print('输出排列')
from itertools import permutations
for p in permutations(items):
    print(p)

# 指定长度
print('指定长度排列')
for p in permutations(items, 2):
    print(p)

# 输出组合，无视排序
print('输出组合')
from itertools import combinations
for p in combinations(items, 3):
    print(p)
print('指定长度组合')
for p in combinations(items, 2):
    print(p)
print('长度1的组合')
for p in combinations(items, 1):
    print(p)
print('允许元素被多次选择')
from itertools import combinations_with_replacement
for p in combinations_with_replacement(items, 3):
    print(p)
