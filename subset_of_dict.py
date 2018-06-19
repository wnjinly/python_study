# coding=utf-8


# 从字典中提取子集


# 最简单的方法是使用字典推导
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key:value for key, value in prices.items() if value > 200}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:vale for key, value in prices.items() if key in tech_names}

# 通过一个元祖序列传给dict()也能做到大多数字典推导,但是字典推导表意更清晰，运行也更快
p1 = dict((key, value) for key, value in prices.items() if value > 200)

# 有时候完成一件事有多种方式。如果对程序性能要求比较高，需要花点时间去做计时测试。计时和性能测试可以参考14.13小结
# 这种方式比字典推导要慢
p2 = {key:prices[key] for key in prices.items()&tech_names}