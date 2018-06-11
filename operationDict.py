# coding=utf-8

# 需要注意的是zip()创建的迭代器只能访问一次
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

prices_and_names = sorted(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)
print(prices_and_names)