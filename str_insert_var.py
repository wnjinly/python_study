# coding=utf-8
# str中插入变量
# 使用format()
s = '{name} has {n} messages.'
print(s.format(name='jinly', n=35))
# use format_map() and vars()
name = 'jinly'
n = 36
print(s.format_map(vars()))

# vars() another feature is can use object instance


class Info():
    """docstring for Info"""

    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('jinly', 35)
print(s.format_map(vars(a)))
# format()相比format_map()的劣势在于，他不可以处理变量缺失的情况
# s.format(name='jinly')
# Traceback (most recent call last):
#   File "D:\Project\python_study\str_insert_var.py", line 20, in <module>
#     s.format(name='jinly')
# KeyError: 'n'
# format_map()定义一个__missing__()方法的字典可以避免这种错误
s1 = '{name} has {m} messages.'


class safesub(dict):
    """docstring for safesub"""

    def __missing__(self, key):
        return '{' + key + '}'


print(s1.format_map(safesub(vars())))
# 将变量替换步骤使用一个工具封装起来
import sys


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'jinly'
n = 35
print(sub('Hello {name}'))
print(sub('You have {n} messages'))
print(sub('Your favorite color is {color}'))
# 讨论：
# python缺乏对变量替换的内置支持导致了有各种不同的解决方案
# 有时会看到字符串格式化代码'%(name) has %(n) messages'
# 还有可能看到字符串模板的使用
# import string
# s = string.Template('$name has $n messages.')
# 然而，format(),format_map()比他们更先进，因此应该优先使用
# format()的好处是它支持字符串格式化的所有操作（对齐，填充，数字格式化等）
