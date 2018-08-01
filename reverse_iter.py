# coding=utf-8
# 反向迭代一个序列
# 使用reversed()函数
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)
# reversed()函数使用条件：
# 仅当对象的大小可预先确定或者对象实现了__reversed__()方法时才能生效
# 如果不符合，必须先将对象转换为一个列表才行
# 这种方式的弊端是：当迭代对象元素很多的话，会消耗大量内存
f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')

# 自定义类上实现__reversed__()方法


class Countdown:
    """docstring for Countdown"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(10)):
    print(rr)
for rr in Countdown(10):
    print(rr)
