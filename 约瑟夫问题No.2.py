from collections import deque
q=deque()

while True:
    n,p,m=map(int,input().split())
    turn=[]
    if n==0 and m==0 and p==0:
        break
    for i in range(p,n+1):
        q.append(i)
    for i in range(1,p):
        q.append(i)
    while len(q)>1:
        for i in range(m-1):
            q.append(q.popleft())
        turn.append(q.popleft())
    turn.append(q.popleft())

    print(f"{','.join(map(str,turn))}")





