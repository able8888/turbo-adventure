def f(n,m):
    if n<m:
        n,m=m,n
    if n//m>1:
        return 'win'

    i=0
    while n//m==1:
        n,m=m,n%m
        i+=1
        if m == 0:
            break
    if i%2==1:
        return 'lose'
    else:
        return 'win'

while True:
    a,b=map(int,input().split())
    if a==0 and b ==0:
        break
    else:
        print(f(a,b))
