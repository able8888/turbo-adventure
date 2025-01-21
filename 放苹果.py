def count_ways_to_divide_balls(M, N):
    memo = {}

    def count_ways(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == 1:
            return 1
        if i >= j:
            result = count_ways(i, j - 1) + count_ways(i - j, j)
        else:
            result = count_ways(i, j - 1)
        memo[(i, j)] = result
        return result

    return count_ways(M, N)


t = int(input())
for _ in range(t):
    M,N = map(int, input().split())
    ways = count_ways_to_divide_balls(M, N)
    print(ways)