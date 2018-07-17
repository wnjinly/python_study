# coding=utf-8
# 字符串解析为令牌流
# 1、确认所有输入文本的序列
# 2、利用正则表达式来定义所有可能出现的令牌，包括空格
# 3、指定令牌扫描顺序，如果顺序不正确扫描就会自动停止
# 	 如果一个模式恰好是另一个模式的子字符串，那么长模式需要些在前面
# 4、使用一个生成器输出

text = 'foo = 23 + 42 * 10'
from collections import namedtuple
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))
def generate_tokens(pat, text):
	Token = namedtuple('Token', ['type', 'value'])
	scanner = pat.scanner(text)
	for m in iter(scanner.match, None):
		yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
	print(tok)

# 过滤空白令牌
print('过滤空白令牌')
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
	print(tok)
