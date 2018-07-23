# coding=utf-8
# 创建或测试正无穷、负无穷和NaN

# 创建
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)

# 测试
import math
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))

# 无穷大执行数学计算后，还是无穷大
print(a + 34)
print(a*10)
print(10/a)

# 两个无穷大使用'=='进行比较，返回True
print(float('inf') == float('inf'))

print(a/a)
print(a + b)

# nan值也可以进行操作，并不会产生异常
print(c + 34)
print(c*10)
print(c/2)
print(math.sqrt(c))
# nan比较返回False,所有判定nan值使用math.isnan()
print(float('nan') == float('nan'))
print(c > 3)
print(math.isnan(c))
# 想改变python对于无穷大和NaN的抛出结果，可以使用fpectl模块
