# coding=utf-8
# 矩形和线性代数运算
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
# 转置
print(m.T)
# 逆矩阵
print(m.I)
# 矩阵乘法
v = np.matrix([[2], [3], [4]])
print('==============')
print(m)
print(v)
print(m*v)

# 行列式
# 2维行列式是矩形面积
# 3维有3种情况，基本是体积
a = np.linalg.det(m)
print(a)

# 特征值
b = np.linalg.eigvals(m)
print(b)

# 线性方程组的解
x = np.linalg.solve(m, v)
print(x)
print(m*x)
print(v)
