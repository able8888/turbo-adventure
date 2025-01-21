def f(i,j):
    if i==N-1:
        return tri[i][j]
    return max(f(i+1,j),f(i+1,j+1))+tri[i][j]
N=int(input())
tri=[]
for _ in range(N):
    tri.append([int(i) for i in input().split()])
    print(f(0,0))
#递归写法会Runtime Error
#下面是用递归写法实现动态优化
from functools import lru_cache
@lru_cache(maxsize=None)
def f(i,j):
    if i==N-1:
        return tri[i][j]
    return max(f(i+1,j),f(i+1,j+1))+tri[i][j]
N=int(input())
tri=[]
for _ in range(N):
    tri.append([int(x) for x in input().split()])
print(f(0,0))
#下面是递推写法
N=int(input())
tri=[]
for _ in range(N):
    tri.append([int(i) for i in input().split()])
dp=[[0]*N for _ in range(N)]
for j in range(N):
    dp[N-1][j]=tri[N-1][j]
for i in range(N-2,-1,-1):
    for j in range(i+1):
        dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+tri[i][j]
print(dp[0][0])



