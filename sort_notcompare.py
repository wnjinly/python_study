# coding=utf-8
from operator import attrgetter


class User:
    """docstring for user"""

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

# 使用lambda排序


def sort_notcompare():
    users = [User(23), User(3), User(43)]
    print(users)
    print(sorted(users, key=lambda x: x.user_id))


# 使用operator.attrgetter()排序
def sort_notcompare1():
    users = [User(23), User(3), User(43)]
    print(sorted(users, key=attrgetter('user_id')))


sort_notcompare()
sort_notcompare1()


# 讨论
# attrgetter()比lambda方式要快点
# attrgetter()还支持多个属性同时输入排序
# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

# 同样在min() and max()中也支持attrgetter()
# min(users, key=attrgetter('user_id'))
# max(users, key=attrgetter('user_id'))
