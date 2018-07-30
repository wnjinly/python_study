# coding=utf-8
# # 迭代，重复执行一种动作
# 迭代器协议：对象需要提供next方法，它要么返回迭代中的下一项
# 要么就引起一个StopIteration异常，以终止迭代
# 解释：可迭代对象需要使用next方法，才能返回下一项
# 直到最后一项全部后，再次next，会返回一个StopIteration异常，结束迭代
# 因此我们通常需要使用python的内置工具，（如for循环，sum，min，max函数等）来连续访问迭代对象

# 手动遍历迭代器
# 遍历迭代器不使用for循环


def manual_iter():
    with open('jalapeño.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass
# 这个例子通过捕获StopIterartion来指示迭代的结尾


# 另一种方案使用一个指定值来标记结尾
with open('jalapeño.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

# 迭代机制：
# next一次返回一个对象，然后停止，直到再遇到next
# 当返回StopIteration异常时，迭代结束
'''
>>> items = [1, 2, 3]
>>> # Get the iterator
>>> it = iter(items) # Invokes items.__iter__()
>>> # Run the iterator
>>> next(it) # Invokes it.__next__()
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
StopIteration
>>>
'''
