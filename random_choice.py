# coding=utf-8
# random choice
import random
values = [1, 2, 3, 4, 5, 6]
# 随机一个数
a = random.choice(values)
print(a)
# 随机多个数
b = random.sample(values, 2)
print(b)
# 打乱选择数字
random.shuffle(values)
print(values)
# 随机整数
c = random.randint(0, 10)
print(c)
# 随机浮点数
d = random.random()
print(d)
# 随机N位二进制数
e = random.getrandbits(200)
print(e)

# 随机种子设定
# random.seed(b'bytedata')
# print(random.random())

# 均匀分布
print(random.uniform(1, 10))
# 高斯分布
print(random.gauss(1, 20))

# 密码学相关的程序中，不建议使用，可以使用ssl模块
