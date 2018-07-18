# coding=utf-8
# 转换或者输出二进制、八进制、十六进制的整数

x = 1234
binx = bin(x)
print(binx)
octx = oct(x)
print(octx)
hexx = hex(x)
print(hexx)
# 不输出前缀
binx = format(x, 'b')
print(binx)
octx = format(x, 'o')
print(octx)
hexx = format(x, 'x')
print(hexx)
# 无符号值
x = -1234
binx = format(2**32 + x, 'b')
print(binx)
# 输出整数
intx = int('4d2', 16)
print(intx)
# python的八进制需要注意加前缀
import os
# os.chmod('script', 0755)
#   File "D:\Project\python_study\convert_int.py", line 27
#     os.chmod('script', 0755)
#                           ^
# SyntaxError: invalid token
os.chmod('jalapeño.txt', 0o755)
