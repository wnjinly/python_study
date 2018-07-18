# coding=utf-8
# numbers rounding
# round基本上是4舍6入，中间位时，py3会保留偶数的一边
a = round(1.23, 1)
print(a)
a = round(1.235, 2)
print(a)

# 需要注意的是当一个值刚好在2个值的中间时，round函数返回离它最近的偶数
a = round(1.5, 1)
print(a)
a = round(2.5)
print(a)
# 有时会有意外情况，由于计算机精度问题，机器已经做了截断处理，因此1.15离1.1更近些
a = round(1.15, 1)
print(a)
# 综上所述，除非对精度没有什么要求，否则尽量避免使用round函数

# round()函数的ndigits为负数时，舍入运算作用在十位、百位、千位等
n = 1325253
a = round(n, -1)
print(a)
a = round(n, -2)
print(a)

# 讨论：
# 如果你的目的只是输出一定宽度的数，不需要使用round函数，只需格式化时指定精度即可
x = 1.23456
a = format(x, '0.2f')
print(a)
# 对于大多数浮点运算会有一点点小的误差是可以理解的。
# 如果不想忍受误差（比如金融领域）就需要考虑decimal模块
