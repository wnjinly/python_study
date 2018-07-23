# coding=utf-8
# 复数的数学运算
# complex(real, imag) usage
a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)
print(a.real)
print(a.imag)
# 共轭复数
print(a.conjugate())
print(a + b)
print(a*b)
print(a/b)
print(abs(a))

import cmath
print(cmath.sin(a))
print(cmath.cos(a))
# 平方根
print(cmath.exp(a))

import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a+2)
print(np.sin(a))
# python的标准数学函数math不能产生复数，需要使用cmath模块

# import math
# math.sqrt(-1)
# Traceback (most recent call last):
#   File "D:\Project\python_study\complex_operation.py", line 31, in <module>
#     math.sqrt(-1)
# ValueError: math domain error

import cmath
a = cmath.sqrt(-1)
print(a)
