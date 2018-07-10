# coding=utf-8
# strip() 可以删除开始或结尾的字符
# 默认删除空白字符
s = ' hello world \n'
print(s)
print(s.strip())

print(s.lstrip())
print(s.rstrip())
# 也可以删除指定字符
t = '-----hello= ===='
print(t)
print(t.strip('-'))
print(t.strip('-= '))
# 需要注意的是strip()不会删除字符串中间的文本
t = '-----hello  world====='
print(t.strip('- ='))
# 想删除中间的空格，可以使用replace()
print(t.replace(' ',''))
# 使用re.sub()也可以达到目的
import re
print(re.sub('\s+',' ', t))

# strip()最佳应用莫过于从文件中读取多行文本
# with open(somefile) as f:
# 	lines = (line.strip() for line in f)
# 	for line in lines:
# 		print(line)


