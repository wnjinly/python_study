# coding=utf-8
# 字符串转换为日期
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)
z = datetime.now()
print(z)
diff = z - y
print(diff)
nice_z = datetime.strftime(z, '%A %B %d %Y')
print(nice_z)

# strptime 性能比较差，所以推荐使用一个解析函数
# 这个函数性能比strptime快7倍，所以处理大量数据建议使用下面函数
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
