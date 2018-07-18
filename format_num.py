# coding=utf-8
# 格式化输入数字
x = 1234.56789
a = format(x, '0.2f')
print(a)
a = format(x, '>10.2f')
print(a)
a = format(x, '<10.2f')
print(a)
a = format(x, '^10.2f')
print(a)
a = format(x, ',')
print(a)
a = format(x, '0,.2f')
print(a)
a = format(x, 'e')
print(a)
a = format(x, '0.2E')
print(a)
# 指定形式为 '[<>^]?width[,]?(.digits)?'
# 字符串格式化中也可以使用
a = 'the value is {:0,.2f}'.format(x)
print(a)

# 指定数字位数后，结果值会根据round函数进行4舍5入后返回
# 如果需要根据地区来显示千位数，可以使用local模块中的函数
# 也可以使用字符串的translate()方法
swap_separators = {ord('.'): ',', ord(','): '.'}
a = format(x, ',').translate(swap_separators)
print(a)

# python还可以使用%进行格式化数字，不过这种方法比format()要差一些
a = '%0.2f' % x
print(a)
# 有些特性无法支持，比如添加千位符
