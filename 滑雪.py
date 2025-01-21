import sys
sys.setrecursionlimit(1<<30)
from functools import lru_cache
R,C=map(int,input().split())
maze=[list(map(int,input().split()))for _ in range(R) ]
dir=[(-1,0),(0,1),(1,0),(0,-1)]
dp=[[0]*C for _ in range(R)]

@lru_cache(maxsize=None)
def dfs(x,y):
    if dp[x][y]!=0:
        return dp[x][y]
    ans=1
    for dx,dy in dir:
        nx,ny=x+dx,y+dy
        if  0<=nx<R and 0<=ny<C and maze[nx][ny]<maze[x][y]:
            ans=max(ans,dfs(nx,ny)+1)
    dp[x][y]=ans
    return dp[x][y]
ans=1
for i in range(R):
    for j in range(C):
        ans=max(ans,dfs(i,j))
print(ans)
