
from collections import Counter

n, m = map(int, input().split())  # 读取 n 和 m
a = list(map(int, input().split()))  # 读取价格列表
b = [input().strip() for _ in range(m)]  # 读取水果清单

# 使用 Counter 来统计水果的出现次数
fruit_counts = Counter(b)

# 将每个水果的出现次数按降序排列
sorted_counts = sorted(fruit_counts.values(), reverse=True)

# 排序价格列表，分别计算最小和最大总价格
a.sort()

min_p = 0
max_p = 0

# 计算最小价格：最少出现的水果与价格最低的水果配对
for i in range(len(sorted_counts)):
    if i < len(a):
        min_p += a[i] * sorted_counts[i]

# 计算最大价格：最多出现的水果与价格最高的水果配对
a.sort(reverse=True)
for i in range(len(sorted_counts)):
    if i < len(a):
        max_p += a[i] * sorted_counts[i]

print(min_p, max_p)