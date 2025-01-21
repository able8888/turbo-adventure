def solve(n, m, nums, operations):
    # 初始化 bit_counts 数组
    bit_counts = [0] * 16
    for num in nums:
        for i in range(16):
            if (num >> i) & 1:
                bit_counts[i] += 1

    delta = 0
    results = []

    for op, value in operations:
        if op == 'C':
            delta = (delta + int(value)) % 65536
        elif op == 'Q':
            i = int(value)
            count = bit_counts[i]
            # 计算增量对第i位的影响
            for j in range(16):
                if (delta >> j) & 1 and (i - j) >= 0:
                    count = n - count if (i - j) % 2 == 0 else count
            results.append(count)

    return results


# 读取输入
n, m = map(int, input().split())
nums = list(map(int, input().split()))
operations = []
for _ in range(m):
    op, value = input().split()
    operations.append((op, value))

# 获取所有查询操作的结果
results = solve(n, m, nums, operations)

# 输出结果
for result in results:
    print(result)



