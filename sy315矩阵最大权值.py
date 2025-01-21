dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(maze,x,y,nowvalue):
    global maxvalue
    if x==n and y==m:
        if maxvalue < nowvalue:
            maxvalue = nowvalue
        return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny] !=-200:
            tmp=maze[x][y]
            nextvalue=nowvalue + maze[nx][ny]
            maze[x][y]=-200
            dfs(maze,nx,ny,nextvalue)
            maze[x][y]=tmp
n,m=map(int,input().split())
maze=[]
maze.append([-200 for x in range(m+2)] )
for i in range(n):
    maze.append([-200]+[int(x) for x in input().split()]+[-200])
maze.append([-200 for x in range(m+2)] )

maxvalue=float('-inf')
dfs(maze,1,1,maze[1][1])
print(maxvalue)

