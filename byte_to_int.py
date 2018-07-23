# coding=utf-8
# 字节字符串解压为一个大整数。或者，大整数转化为一个字节字符串
# 主要应用于密码学和网络
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
a = len(data)
print(a)
# little从低位开始构建（小端），big从高位开构建（大端）
b = int.from_bytes(data, 'little')
print(b)
b = int.from_bytes(data, 'big')
print(b)

x = 94522842520747284487117727783387188
a = x.to_bytes(16, 'big')
print(a)
b = x.to_bytes(16, 'little')
print(b)

# 使用struct方式
import struct
# 大端，2个无符号长整型
hi, lo = struct.unpack('>QQ', data)
# 左移64位
a = (hi << 64) + lo
print(a)
# 当一个整数范围过大时，使用int.to_bytes()方法可能会报错
# 可以使用int.bit_length()解决
x = 523 ** 23
print(x)
# bit_length()位数，divmod()返回商和余数
nbtyes, rem = divmod(x.bit_length(), 8)
# 确定8进制位数
if rem:
    nbtyes += 1
a = x.to_bytes(nbtyes, 'little')
print(a)
