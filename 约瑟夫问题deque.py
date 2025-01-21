from collections import deque
q=deque()
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    for i in range(1,n+1):
        q.append(i)
    while len(q)>1:
        for i in range(m-1):
            q.append(q.popleft())
        q.popleft()
    print(q.pop())

