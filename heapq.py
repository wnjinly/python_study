#heapq方法讨论
#heapq还有nlargest()和nsmallest()俩种方法，用来求最大或最小的N个元素
import heapq
nums = [123,32,3,32,31,54,32,536,6343,132542]
#3个最大值
print(heapq.nlargest(3, nums))
#3个最小值
print(heapq.nsmallest(3, nums))
#更复杂的数据结构中使用
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
#three smallest price datas
cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
#three largest price datas
expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list[nums]
#将list转变成堆
heapq.heapify(heap)
#堆数据结构的特点，heap[0]永远是最小的
heap
#>>>>[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
#heapq.heappop()方法会将第一个元素弹出（这种操作时间复杂度为O(log N)，N是堆的大小）
heapq.heappop(heap)
#>>>>-4
#使用方法比较
#当查找元素个数相对比较小时，nlargest()和nsmallest()比较合适。
#只查找最小值和最大值时，使用min()和max()
#如果查找的元素个数和集合大小接近时，通常先排序，再切片比较快sorted(items)[:N]或者sorted(items)[-N:]