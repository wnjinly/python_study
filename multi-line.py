# coding=utf-8

import re

# 多行匹配
# 1、(?:.|\n)
text2 = '''/* this is a
multiline comment */
'''
comment = re.compile(r'/\*(.*?)\*/')
print(comment.findall(text2))

comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment1.findall(text2))

# 2、re.DOTALLA让(.)匹配包括换行符在内的任意字符
comment2 = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment2.findall(text2))

