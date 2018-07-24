# coding=utf-8
# 大型数组运算
# 使用numpy
import numpy as np
ax = np.array([1, 23, 4, 32])
ay = np.array([5, 6, 4, 1])
print(ax)
print(ay)
print(ax*2)
print(ax + 10)
print(ax + ay)


def f(x):
    return 2*x**2 - 2*x + 7


a = f(ax)
print(a)

print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)
grid += 10
print(grid)

# 多维数组
a = np.array([[1, 2, 3, 4], [43, 2, 32, 1], [342, 31, 321, 13]])
print(a)
print(a[1])
print(a[:, 1])
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a + [100, 100, 100, 100])
# 将大于10的数都变为10
print(np.where(a < 10, a, 10))
