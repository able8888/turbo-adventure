def count_ways_to_divide_balls(M, N):
    memo = {}

    def count_ways(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return 1
        if j == 1:
            return 1
        if i >= j:
            result =  count_ways(i - j, j)+count_ways(i,j-1)
        else:
            result = count_ways(i, j-1)
        memo[(i, j)] = result
        return result

    return count_ways(M, N)

n,k=map(int,input().split())
print(count_ways_to_divide_balls(n-k,k))