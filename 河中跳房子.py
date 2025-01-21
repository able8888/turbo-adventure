L,M,N=map(int,input().split())
rock=[0]
for i in range(N):
    rock.append(int(input()))
rock.append(L)

def check(x):
    num=0
    now=0
    for i in range(1,N+1):
        if rock[i]-now<x:
            num+=1
        else:
            now=rock[i]
    if num>M:
        return True
    else:
        return False
l,r=0,L+1
ans=-1
while l<r:
    mid=(l+r)//2
    if check(mid):
        ans=mid
        l=mid+1
print(ans)