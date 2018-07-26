# coding=utf-8
# 包含时区的日期操作，pytz
from datetime import datetime
from pytz import timezone
d = datetime(2018, 7, 26, 13, 50, 0)
print(d)
# local the date for central
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# convert to Shanghai
bang_d = loc_d.astimezone(timezone('Asia/Shanghai'))
print(bang_d)
print('===============')
# 本地时间转换
# 需要注意的是，某些国家会使用夏令时
# 因此转换时，需要使用normalize()方法
from datetime import timedelta
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
# 错误方式
later = loc_d + timedelta(minutes=30)
print(later)
# 正确方式
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)
print('===============')

# 最佳处理方式，为了不考虑夏令时问题，处理本地化时
# 首先转化为UTC时间，进行存储，再转化为对应时区时间
print(loc_d)
import pytz
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))