# coding=utf-8

# 字符串搜索和替换
# 对于简单的字面模式，直接使用str.replace()即可
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
# 对于复杂模式，使用re.sub()
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))
# 同样如果需要多次替换，可以对正则表达式进行预编译
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2',text))
# 对于更加复杂的替换，可以传递一个回调函数
from calendar import month_abbr
def change_date(m):
	mon_name = month_abbr[int(m.group(1))]
	return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

print(datepat.sub(change_date, text))
# re.subn()可以用来知道替换了多少次
newtext, n = datepat.subn(r'\3-\1-\2',text)
print(newtext)
print(n)


# 忽略大小写，可以使用re.IGNORECASE
text = 'UPPER PYTHON, lower python, Mixed Python'
a = re.findall('python',text,flags=IGNORECASE)
print(a)
b = re.sub('python', 'snake', text, flags=IGNORECASE)
print(b)
