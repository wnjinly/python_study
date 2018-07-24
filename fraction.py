# coding=utf-8
# fractions operation
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a+b)
print(a*b)
c = a*b
# 分子
print(c.numerator)
# 分母
print(c.denominator)
# converting to a float
d = float(c)
print(d)

# 限制分母
print(c.limit_denominator(8))

# converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
