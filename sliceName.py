# coding=utf-8

# 切片命名，主要作用便于维护，使代码更加清晰，便于阅读


items = [0, 1, 2, 3, 4, 5, 6]
# 使用slice()方法命名

a = slice(2, 8, 2)
a.start
a.stop
a.step

# 使用切片的indices(size)可以将还可以将它映射到一个固定大小的序列上。避免抛出异常
# 这个方法返回一个三元组
a.indices(len(items))

# >>>（2,8,2）

for i in range(*a.indices(len(items))):
    print(items[i])
