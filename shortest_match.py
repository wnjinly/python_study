# coding=utf-8

import re
# 通过?来表示最短匹配
# 无?是正则表达式默认是最长匹配
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text1))

str_sht_pat = re.compile(r'\"(.*?)\"')
print(str_sht_pat.findall(text1))