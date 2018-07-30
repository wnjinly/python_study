# coding=utf-8
# 构建了一个自定义容器，容器里包含有列表、元祖或者其他可迭代对象
# 想直接在容器的对象上执行迭代操作

# 实现方法：
# 定义一个__iter__()方法，将迭代操作代理到容器内部的对象上去
class Node:	
	"""docstring for Node"""
	def __init__(self, value):
		self._value = value
		self._children = []
	def __repr__(self):
		return 'Node({!r})'.format(self._value)		

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)
	# iter()调用__iter__()方法来返回迭代器对象

if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)
	for ch in root:
		print(ch)