# coding=utf-8


from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
# 计数器
word_counts = Counter(words)

print(word_counts)
top_three = word_counts.most_common(3)

print(top_three)
# 更新是元素次数
word_counts.update(['eyes'])
print(word_counts)
# counter 很容易和数学运算操作结合，可以自动计算
