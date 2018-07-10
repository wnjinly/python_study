# coding=utf-8
# 清理文本字符串
s = 'pýtĥöñ\fis\tawesome\r\n'
# 方法一：
# 1. 清理空白字符
# 创建一个转换表格然后使用translate()
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print(a)
# 2. 删除所有的和音符
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(
    sys.maxunicode) if unicodedata.combining(chr(c)))
# 3. 使用unicodedata.normalize()标准化为分解形式的字符
b = unicodedata.normalize('NFD', a)
print(b)
# 4. 调用translate()删除所有重音符
c = b.translate(cmb_chrs)
print(c)
# 方法2：
# I/O解码与编码
b = unicodedata.normalize('NFD', a)
c = b.encode('ascii', 'ignore').decode('ascii')
print(c)
# 讨论：
# 从性能上来说代码越少性能越好
# 对于简单的替代操作，str.replace()会比translate()或者正则表达式快很多
# 但是对于复杂字符的重新映射或删除操作的话，translate()方法会非常快
# 实际应用中需要尝试不同的方式并评估他们
