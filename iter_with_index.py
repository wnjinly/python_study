# coding=utf-8
# 迭代一个序列的同时追踪正在被处理的元素索引
# 使用enumerate()
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 从1开始
for idx, val in enumerate(my_list, 1):
    print(idx, val)


# 遍历文件时，在错误消息中使用行定位时很有用
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


# 追踪某些值在列表中的位置
from collections import defaultdict
word_summary = defaultdict(list)
with open('somefile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

# 讨论：定义一个计数变量时，使用enumerate()更加优雅
# for lineno, line in enumerate(f):
# 	  ...

# enumerate()返回的是对象实例，是一个迭代器。返回连续的包含一个计数和一个值得元组
# 元组的值通过在传入序列上调用next()返回。
# 另外需要注意：在一个元组序列上使用enumerate()时
# data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

# Correct!
# for n, (x, y) in enumerate(data):
#     ...
# # Error!
# for n, x, y in enumerate(data):
#     ...
