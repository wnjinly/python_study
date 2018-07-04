# coding=utf-8

filename = 'spam.txt'
print(filename.endswith('.txt'))
url = 'http://www.baidu.com'
print(url.startswith('http'))

# 检查多个匹配时，将所有匹配放入一个元祖
import os

filenames = os.listdir('.')
print(filenames)
list = [name for name in filenames if name.endswith(('.git', 'book'))]
print(list)

# 检查是否存在某些内容时
if any(name.endswith(('.c', '.git')) for name in os.listdir('.')):
    print('exist')
