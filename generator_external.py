# coding=utf-8
# 带有外部状态的生成器函数
# 实现方法：
# 实现为一个类，然后把生成器函数放到__iter__()中去
from collections import deque


class linehistory:
    """docstring for linehistory"""

    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


# 访问
with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
