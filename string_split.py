# coding=utf-8

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
# 分割多个字符
print(re.split(r'[;,\s]\s*', line))

# re.split()使用时，如果正则表达式中有一个括号分组。那么被匹配的文本也将出现在结果列表中
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# 分组的好处在于，使用切片可以重新构造一个新的输出字符串
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
print(''.join(v+d for v, d in zip(values, delimiters)))

# 如果不想被匹配的文本出现在列表中可使用(?:...)
print(re.split(r'(?:,|;|\s)\s*', line))
