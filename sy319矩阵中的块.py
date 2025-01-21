from collections import deque
n,m=map(int,input().split())

matrix=[]
matrix.append([-1]*(m+2))
for i in range(n):
    matrix.append([-1]+[int(x) for x in input().split()]+[-1])
matrix.append([-1]*(m+2))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
#bfs
def bfs(x,y):
    q=deque([(x,y)])
    inq.add((x,y))
    while q:
        front=q.popleft()
        for i in range(4):
            nx=front[0]+dx[i]
            ny=front[1]+dy[i]
            if matrix[nx][ny]==1 and (nx,ny) not in inq:
                inq.add((nx,ny))
                q.append((nx,ny))
#主循环
sum = 0
inq = set()
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j] == 1 and (i,j) not in inq:
            bfs(i,j)
            sum += 1

print(sum)


