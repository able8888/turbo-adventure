dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(maze,x,y,nowvalue):
    global maxvalue
    if x==n and y==m:
        if nowvalue>maxvalue:
            maxvalue=nowvalue
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]==0:
            nextvalue = nowvalue + w[nx][ny]
            maze[x][y]=1
            tmp=w[x][y]
            w[x][y]=-200
            dfs(maze,nx,ny,nextvalue)
            maze[x][y]=0
            w[x][y]=tmp

maxvalue=float('-inf')
n,m=map(int,input().split())
maze=[]
maze.append([-1 for i in range(m+2)])
for x in range(n):
    maze.append([-1]+[int(x) for x in input().split()]+[-1])
maze.append([-1 for i in range(m+2)])
w=[]
w.append(-200 for i in range(m+2))
for x in range(n):
    w.append([-200]+[int(x) for x in input().split()]+[-200])
w.append(-200 for i in range(m+2))
dfs(maze,1,1,w[1][1])
print(maxvalue)