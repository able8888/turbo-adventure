p=int(input())
a=sorted(list(map(int,input().split())))
i,j,cnt=0,len(a)-1,0
while i<j:
    if a[i]<=p:
        p-=a[i]
        i+=1
        cnt+=1
    elif cnt:
        cnt-=1
        p+=a[j]
        j-=1
    else:
        break

print(cnt+(a[i] <= p))



