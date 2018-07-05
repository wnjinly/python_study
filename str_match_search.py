# coding=utf-8

# 字符串匹配和搜索

# 简单匹配可以使用str.endswith(),str.startwith(),str.find()
text = 'yeah, but no, but yeah, but no, but yeah'
text.startswith('yeah')
text.endswith('yeah')
print(text.find('no'))

# 对于复杂匹配需要正则表达式
# 而如果想要多次匹配的话，可以先使用re.compile()进行编译正则表达式字符串
# 再使用match(),findall()或者finditer()
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
	print('yes')
else:
	print('no')

if datepat.match(text2):
	print('yes')
else:
	print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# 正则表达式分组匹配
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('05/07/2018')
month,day,year = m.groups()
print(month)
print(day)
print(year)

# findall()查找所有匹配
m = datepat.findall(text)
print(m)
for month,day,year in m:
	print('{}-{}-{}'.format(year,month,day))

# finditer()迭代方式返回匹配
for n in datepat.finditer(text):
	print(n.groups())

# match()方式只是匹配字符串开始部分
# 如果想要精准匹配，在正则表达式末尾使用$
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012'))

# 预编译会减少性能消耗，如果需要大量匹配和搜索推荐使用