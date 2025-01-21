dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(maze,x,y,nowvalue,nowpath):
    global maxvalue,maxpath
    if x==n and y==m:
        if maxvalue < nowvalue:
            maxvalue = nowvalue
            maxpath=nowpath[:]
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny] !=-999:
            tmp=maze[x][y]
            maze[x][y]=-999
            nextvalue=maze[nx][ny]+nowvalue
            nowpath.append((nx,ny))
            dfs(maze,nx,ny,nextvalue,nowpath)
            maze[x][y]=tmp
            nowpath.pop()

n,m=map(int,input().split())
maze=[]

maxvalue=float('-inf')
maxpath=[]
maze.append([-999 for x in range(m+2)])
for x in range(n):
    maze.append([-999]+[int(x) for x in input().split()]+[-999])
maze.append([-999 for x in range(m+2)])
dfs(maze,1,1,maze[1][1],[(1,1)])
for x,y in maxpath:
    print(x,y)





