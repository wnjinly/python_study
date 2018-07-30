# coding=utf-8
# 使用生成器生成新的迭代模式


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

# 生成器不同于普通函数，只能用于迭代操作
# 生成器和for是好搭档，for语句会自动处理迭代终止时的状况
