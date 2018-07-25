# coding=utf-8
# 找到指定日期前的最后一个星期（比如星期五）
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wedensday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
        # 开始日期和目标日期映射到数组上，0为星期一
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    # 通过取模运算，计算出到达目标日期需要多少天
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    # 用开始日期减去时间差得到目标日期
    target_date = start_date - timedelta(days=days_ago)
    return target_date


a = get_previous_byday('Sunday', datetime(2018, 6, 15))
print(a)

# 使用dateutil方案
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)
# next friday
print(d + relativedelta(weekday=FR))
# last friday
print(d + relativedelta(weekday=FR(-1)))
