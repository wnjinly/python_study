# coding=utf-8
# 字节字符串操作
# 字节字符串操作支持大多数的文本字符串的内置操作

# 比如
data = b'Hello World'
a = data[0:5]
print(a)
b = data.startswith(b'Hello')
print(b)
c = data.split()
print(c)
d = data.replace(b'Hello', b'Hello jinly')
print(d)

# 字节数组操作
data = bytearray(b'Hello World')
a = data[0:5]
print(a)
b = data.startswith(b'Hello')
print(b)
c = data.split()
print(c)
d = data.replace(b'Hello', b'Hello jinly')
print(d)

# 使用正则表达式，但是正则表达式也必须是字节串
data = b'FOO:BAR,SPAM'
import re
# re.split('[:,]',data)
# Traceback (most recent call last):
#   File "D:\Project\python_study\byte_str.py", line 30, in <module>
#     re.split('[:,]',data)
#   File "C:\Python36\lib\re.py", line 212, in split
#     return _compile(pattern, flags).split(string, maxsplit)
# TypeError: cannot use a string pattern on a bytes-like object
e = re.split(b'[:,]', data)
print(e)

# 多数情况下文本字符串操作和字节字符串相同
# 但也有些例外，如索引操作，字节字符串返回的是整数
b = b'Hello World'
a = b[0]
print(a)
# 此外，字节字符串不能很好地打印出来，除非先行解码
print(b)
print(b.decode('ascii'))
# 类似的格式化操作也不适用与字节字符串
# a = b'{} {} {}'.format(b'ACME', 100, 490.1)
# print(a)
# Traceback (most recent call last):
#   File "D:\Project\python_study\byte_str.py", line 49, in <module>
#     a = b'{} {} {}'.format(b'ACME', 100, 490.1)
# AttributeError: 'bytes' object has no attribute 'format'
a = b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
print(a)
# 正确的格式化
a = '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
print(a)
# 还需要注意的是，使用字节字符串操作可能会改变一些操作语义
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

import os
print(os.listdir('.'))
# 文件名未进行解码返回
print(os.listdir(b'.'))
# 最后不推荐使用字节字符串，虽然它执行速度上会快一些。
