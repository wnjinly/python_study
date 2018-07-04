# coding=utf-8

# 使用操作系统shell匹配文本字符串
# fnmatch模块
# fnmatch() and famatchcase() 区别：
# fnmatch()是根据操作系统来判定大小写敏感规则的
# 	mac和linux大小写敏感，windows大小写不敏感
# fnmatchcase 则是严格执行匹配的
from fnmatch import fnmatch, fnmatchcase
# fnmatch usage
a = fnmatch('foo.txt', '*.txt')
print(a)
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
filters = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(filters)

b = fnmatch('foo.txt', '*.TXT')
print(b)

c = fnmatchcase('foo.txt', '*.TXT')
print(c)

# fnmatch()介于简单的字符串方法和强大的正则表达式之间。当需要简单的匹配时是非常有用的
# example
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

addrs = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(addrs)
