from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(n,m,x,y,mat):
    inq=set()
    queue=deque()
    queue.append((x,y))
    inq.add((x,y))
    prev=[[(-1,-1)]*m for _ in range(n)]

    while queue:
        x,y=queue.popleft()
        if x==n-1 and y==m-1:
            return prev
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and mat[nx][ny]==0 and (nx,ny)not in inq:
                inq.add((nx,ny))
                prev[nx][ny]=(x,y)
                queue.append((nx,ny))
    return None



