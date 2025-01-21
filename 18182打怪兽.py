from collections import defaultdict
nCases=int(input())
for _ in range(nCases):
    situation='alive'
    n,m,b=map(int,input().split())
    a=defaultdict(list)
    for _ in range(n):
        x,y=map(int,input().split())
        a[x].append(y)
    for x in sorted(a):
        if len(a[x])<=m:
            b -= sum(a[x])
        else:
            a[x].sort(reverse=True)
            b -= sum(a[x][:m])
        if b<=0:
            situation = x
            break
    print(situation)
