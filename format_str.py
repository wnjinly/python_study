# coding=utf-8
# 格式化字符串为指定列宽
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))

print(textwrap.fill(s, 40))

print(textwrap.fill(s, 40, initial_indent='	'))

print(textwrap.fill(s, 40, subsequent_indent='	'))
# textwrap模块对于打印字符串非常有用，特别是当希望输出自动匹配到终端大小时
# import os
# print(os.get_terminal_size().columns)
# fill()还可以接受一些其他参数来控制tab，语句结尾等。参阅textwrap.TextWrapper文档
