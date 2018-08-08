# coding=utf-8
# 跳过可迭代的开始部分
# 跳过一个可迭代对象的开始部分
# itertools.dropwhile()用法
with open('somefile.txt') as f:
    for line in f:
        print(line, end='')
print('==============')
# 过滤开头,使用dropwhile()
from itertools import dropwhile
with open('somefile.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
print('=================')
# 如果明确知道了元素个数，使用itertools.islice()
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
# None参数代表所有，下面语句代表[3:]
# islice(items, None, 3)表示[:3]
for x in islice(items, 3, None):
    print(x)
print('================')

# 全部过滤
with open('somefile.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

print('冗余代码方式')
# 函数dropwhile()和islice()就是帮助函数，可以避免冗余代码,如下面
with open('somefile.txt') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    while line:
        print(line, end='')
        line = next(f, None)
