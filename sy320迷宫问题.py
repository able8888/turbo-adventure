from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#bfs
def bfs(x,y,n,m,maze):
    q=deque([(0,(x,y))])
    inq = set()
    inq.add((x,y))
    while q:
        step,(x,y) = q.popleft()
        if x==n and y==m:
            return step
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if maze[nx][ny] == 0 and (nx,ny) not in inq:
                q.append((step+1,(nx,ny)))
                inq.add((nx,ny))
    return -1
if __name__ == '__main__':

    n,m=map(int,input().split())
    maze=[]
    maze.append([-1]*(m+2))
    for i in range(n):
        maze.append([-1]+[int(x) for x in input().split()]+[-1])
    maze.append([-1]*(m+2))
    print(bfs(1,1,n,m,maze))
