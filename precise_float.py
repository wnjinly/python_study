# coding=utf-8
# 精确的浮点数运算，不允许误差
# 正常的浮点运算是有误差的
a = 4.1
b = 2.1
print(a+b)
print((a+b) == 6.2)
# 如果想要避免误差，可以使用decimal模块
from decimal import Decimal
a = Decimal('4.1')
b = Decimal('2.1')
c = a + b
print(a+b)
print((a+b) == Decimal('6.2'))

# 另外，decimal可以允许你控制计算的每一个方面
print(a/b)
from decimal import localcontext
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)

# 虽然decimal有更高的精度，但是需要根据实际情况使用它
# 真实世界很少要求普通浮点数提供17位精度，因此运算过程中有误差是被允许的
# 此外，原生的浮点运算速度要快很多
# 但也不能完全忽略误差
nums = [1.23e+18, 1, -1.23e+18]
a = sum(nums)
print(a)
# 解决上面误差
import math
a = math.fsum(nums)
print(a)
# 结论：decimal主要运用在金融领域
# 其他领域运算，需要根据实际情况选择合适的解决方案
