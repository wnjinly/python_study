# coding=utf-8
# 文本标准化，便于比较字符串

s1 = 'hello world\u00f1o'
s2 = 'hello worldn\u0303o'
print(s1 == s2)
print(s1)
print(s2)

# 使用unicodedata模块进行标准化
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)

t1 = unicodedata.normalize('NFD', s1)
print(t1)
# 不为和音字符，则转化为
t3 = ''.join(c for c in t1 if not unicodedata.combining(c))
print(t3)
