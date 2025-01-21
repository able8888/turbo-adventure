t=int(input())
for _ in range(t):
    n=int(input())
    square=set()
    i=0
    while 2**i<10**6:
        square.add(2**i)
        i+=1
    sum=0
    for j in range(1,n+1):
        if j in square:
            sum+=-j
        else:
            sum+=j
    print(sum)
#超时
import math
t=int(input())
for _ in range(t):
    n=int(input())
    sum=0
    if n % 2 == 1:
        sum=(n-1)*n//2+n
    else:
        sum=(n+1)*n//2
    maxp=int(math.log2(n))
    for i in range(maxp+1):
        sum-=2*(2**i)
    print(sum)



