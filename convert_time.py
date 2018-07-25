# coding=utf-8
# 时间转换
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c)
print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)

# 指定的日期和时间
from datetime import datetime
a = datetime(2018, 7, 25)
print(a)
print(a + timedelta(days=10))

b = datetime(2018, 8, 25)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

# datetime会自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
a = datetime(2013, 3, 1)
b = datetime(2013, 2, 28)
print(a - b)

# 复杂日期处理 dateutil,处理时区，模糊时间范围，节假日计算等
# 处理月份
a = datetime(2012, 9, 23)
# a + timedelta(months=1)
# Traceback (most recent call last):
#   File "D:\Project\python_study\convert_time.py", line 36, in <module>
#     a + timedelta(months=1)
# TypeError: 'months' is an invalid keyword argument for this function
from dateutil.relativedelta import relativedelta
b = a + relativedelta(months=1)
print(b)
print(a + relativedelta(months=+4))

b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d)
print(d.months)
print(d.days)
