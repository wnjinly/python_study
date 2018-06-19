# coding=utf-8
# 通过下角标访问列表或者元祖中的元素代码，代码让人难以理解。
# 使用collections.nametuple(),可以解决这个问题

from collections import namedtuple
# 这个函数实际是返回一个python中标准元祖类型子类的一个工厂方法。
# 传递一个类型名和字段后，它会返回一个类。
# 然后对于这个类，可以初始化类、为定义的字段传值等
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('john@example.com', '2018-6-19')
print(sub)
# 访问属性
print(sub.addr)
print(sub.joined)

# nametuple看起来想一个普通实例，但它跟元祖类型是可交换的，支持所有普通元祖操作
print(len(sub))

addr, joined = sub
print(addr)
print(joined)

# 元祖命名的主要作用就是将你从下标操作中解脱出来。
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost1(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total = s.shares*s.price
    return total

# 元祖命名的另一个作用是代替字典，因为字典会使用更多的内存空间。
# 如果要创建一个非常大的包含字典的数据结构，那么使用命名元祖更加高效。
# 但是有一点需要注意，命名元祖是不能更改的
s = Stock('SDFSA', 100, 3434)
# 对命名元祖赋值会报错
# s.shares = 75
# >>>>
# Traceback (most recent call last):
# File "D:\Project\python_study\nametuple.py", line 31, in <module>
#     Stock = nametuple('Stock', ['name', 'shares', 'price'])
# NameError: name 'nametuple' is not defined

# 如果非要改变属性的值，可以使用_repalce()方法
s = s._replace(shares = 75)
print(s)

# _replace() 方法还有一个很有用的特性
# 当你命名的元祖拥有可选或缺失字段时，它是一个非常方便的填充数据的方法。
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
	return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

# 最后，如果你需要的是一个需要更新很多实例属性的高效数据结构，那么命名元祖并不是最佳选择。
# 这时候需要一个包含__slots__方法的类（参考8.4小节）