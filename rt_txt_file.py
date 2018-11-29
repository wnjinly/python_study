# coding=utf-8
# 读取不同编码的文本文件
# 解决方案：使用 t 表示文本模式，有效避免各种编码问题
with open('somefile.txt','rt') as f:
	data = f.read()

with open('somefile.txt','rt') as f:
	for line in f:
		print(line)

# 写入
# wt 替代文件内容
# at 末尾添加内容
# encoding 参数可以指定文件的编码
# 指定编码可能会造成错误。
# 如果编码一直错误可以使用errors参数来处理错误。 errors='replace' errors='ignore'
# 但不推荐如此。

# Unix和windows中换行符是不一样的（分别是n和rn）。
# python默认会转换为单个\n。
# 如果不希望如此可以使用参数newline=''