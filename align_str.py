# conding=utf-8
# 字符串对齐
text = 'Hello World'
# 对齐操作方法：ljust(),rjust(),center()
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
# 还可填充字符
print(text.ljust(20,'='))
print(text.center(20,'*'))
# format()也可用来对齐
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
# 格式化多个值时
print('{:>10s}{:>10s}'.format('hello','world'))
# format()的好处是它可以用来格式化任何值
x = 1.2325424
print(format(x, '>10'))
print(format(x, '^10.2f'))
# 讨论：format()在新版本中推荐使用
# 比ljust(),rjust(),center()等方法更加通用