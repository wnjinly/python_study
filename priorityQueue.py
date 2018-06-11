# coding=utf-8
import heapq


class PriorityQueue():
    """docstring for PriorityQueue"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 使用heappush在队列中插入一个元祖
        # 由于推数据结构的特性，-priority，保证了每次推出的总是优先级最高的
        # index保证了，当优先级相同的情况下，不会出错
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 推出最后的元素
        return heapq.heappop(self._queue)[-1]


class Item:
    """docstring for Item"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
