# coding=utf-8

# 转换并同时计算数据

# 使用一个生成器表达式参数
# 当生成器表达式作为一个单独参数传递给函数时，并不需要多加一个括号
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)

import os
print(os.listdir())
files = os.listdir('cookbook')
if any(name.endswith('.py') for name in files):
	print('There be python!')
else:
	print('Sorry, no python.')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)


# 不使用生成器表达式
# 这种方式，会先创建一个额外的列表，会使用更多的内存。所以是不推荐的方式
s = sum([x*x for x in nums])

# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)