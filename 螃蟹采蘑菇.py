from collections import deque
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
dir= [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(x_1,y_1,x_2,y_2):
    inq=set()
    q=deque()
    inq.add((x_1,y_1,x_2,y_2))
    q.append((x_1,y_1,x_2,y_2))

    while q:
        x1,y1,x2,y2=q.popleft()
        if a[x1][y1]==9 or a[x2][y2]==9:
            return True
        for dx,dy in dir:
            nx1,ny1=x1+dx,y1+dy
            nx2,ny2=x2+dx,y2+dy
            if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n:
                if a[nx1][ny1]!=1 and a[nx2][ny2]!=1:
                    if (nx1,ny1,nx2,ny2) not in inq:
                        q.append((nx1, ny1, nx2, ny2))
                        inq.add((nx1, ny1, nx2, ny2))
    return False
#找螃蟹开始的位置
b=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==5:
            b.append([i,j])
if len(b)==2:
    result=bfs(b[0][0],b[0][1],b[1][0],b[1][1])
    print('yes' if result else 'no')
else:
    print('no')
