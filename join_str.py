# coding=utf-8
# 拼接字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))
# +
a = 'Is Chicago'
b = 'Not Chicago?'
c = a + ' ' + b
print(c)
print('{} {}'.format(a, b))
d = 'Is Chicago' 'Not Chicago?'
print(d)
# 讨论：
# 使用+去连接大量字符串效率很低，因为+会引起内存复制和垃圾回收操作
# 最好的方法是先收集所有字符串片段然后再将他们连接起来
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
# 另外尽量避免字符串连接操作，如打印时
print(a + ':' + b + ':' + c)  # 不推荐
print(':'.join([a, b, c]))  # 不推荐
print(a, b, c, sep=':')  # 推荐
# 另外I/O操作时需要注意，选择合适的方法
# f.write(chunk1 + chunk2)

# f.write(chunk1)
# f.write(chunk2)

# 当字符串很小时，第一种方法比较合适。
# 当字符串很大时，第二种方法更为合适

# 最后构建大量小字符串的输出代码，最好考虑使用生成器函数，利用yield语句生成输出片段
# 生成器函数并不需要知道使用细节，只负责生成器字符串片段就行


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


# 可以使用多种方式进行输出
# join
text = ''.join(sample())
print(text)
# 定向I/O
for part in sample():
    f.write(part)
# 混合方案


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)


with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
