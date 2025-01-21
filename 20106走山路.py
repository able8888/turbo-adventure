import heapq
m,n,p=map(int,input().split())
mat=[input().split() for _ in range(m)]
queries=[tuple(map(int,input().split())) for _ in range(p)]

def dijkstra(m,n,mat,queries):
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    result=[]
    for a,b,c,d in queries:
        if mat[a][b]=='#' or mat[c][d]=='#' :
            result.append('NO')
            continue
        heap=[(0,a,b)]
        dist={(a,b):0}
        found=False

        while heap:
            cost,i,j=heapq.heappop(heap)
            if (i,j)==(c,d):
                result.append(dist[(i,j)])
                found=True
                break
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] != '#':
                    try:
                        new_cost=cost+abs(int(mat[ni][nj])-int(mat[i][j]))
                    except ValueError:
                        continue
                    if (ni, nj) not in dist or new_cost < dist[(ni, nj)]:
                        dist[(ni,nj)] = new_cost
                        heapq.heappush(heap,(new_cost,ni,nj))
        if not found:
            result.append('NO')
    return(result)
print('\n'.join(map(str,dijkstra(m,n,mat,queries))))





