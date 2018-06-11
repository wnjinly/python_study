# coding=utf-8

# 删除序列相同元素并保持顺序

# 可hashable类型指的是这个object有一个不可变的哈希值，如：字符串、元祖

# 可hashable类型时，使用下面方式即可


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# 不可hashable类型，消除不可哈希元素
def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# 讨论
# 如果只是想删除重复元素使用set()即可，但是其会打乱元素顺序


# 拓展
# 读取文件消除重复行
with open(somefile, 'r') as f:
    for line in dedupe(f):
        pass
