# coding=utf-8

# 找出大于0的值
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

value = [n for n in mylist if n > 0]

# 使用生成器可以更节省内存
value1 = (n for n in mylist if n > 0)
for i in value:
    print(i)

# 复杂情况可以使用内建函数filter()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

# 列表推到和生成器表达式，既可以在过滤时进行转换数据，又能对指定条件的值进行替换


# 过滤工具itertools.compress()，使用俩个序列筛选出需要的数据
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

# 生成一个bool序列
more5 = [n > 5 for n in counts]
# 进行筛选
list(compress(addresses, more5))
