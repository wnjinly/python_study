# coding=utf-8
# 顺序迭代合并后的排序迭代对象
import heapq
a = [2,3,4,5]
b = [343,4,5,6,43]
for c in heapq.merge(a, b):
	print(c)

# heapq.merge 可迭代特性意味着它不会立马读取所有序列。
# 这意味着在非常长序列中使用它，也不会有太大的开销
with open('sorted_file_1', 'rt') as file1, \
	open('sorted_file_2', 'rt') as file2, \
	open('merged_file', 'wt') as outf:
	for line in heapq.merge(file1, file2):
		outf.write(line)

# 需要注意的是heapq.merge() 不会自己排序