# coding=utf-8

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# find keys in common
a.keys() & b.keys()
# find keys in a that are not in b
a.keys() - b.keys()
# find items in common
a.items() & b.items()

# 去除字典中某些keys
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
