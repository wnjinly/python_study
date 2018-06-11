# coding=utf-8

from collections import OrderedDict
import json
# orderedDict 会创建一个有序的字典
# orderedDict内部是一个双向链表。因此大小是普通dict的双倍。当数据量很大的时候需要权衡下是否使用
d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# 将有序字典存储到json中
json.dumps(d)
