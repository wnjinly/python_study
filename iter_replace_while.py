# coding=utf-8
# 迭代器代替while无限循环
# CHUNKSIZE = 8192

# def reader(s):
#     while True:
#         data = s.recv(CHUNKSIZE)
#         if data == b'':
#             break
#         process_data(data)

# 使用iter()来代替
# def reader2(s):
#     for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
#         pass
#         # process_data(data)
#
#
# 具体例子
import sys
f = open('passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)

# 迭代器的好处：
# 惰性计算，自动终止。操作和序列底层分离
