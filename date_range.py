# coding=utf-8
# 指定一个日期，从这个日期开始循环，循环区域为这个日期所在的月份
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    # 获取今天日期，并把开始日期设置为1号
    if start_date is None:
        start_date = date.today().replace(day=1)
    # 计算出本月的天数
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    # 获得本月的最后一天
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


# 打印日期，方案一
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

# 方案二，更好的
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1), timedelta(days=1)):
    print(d)
