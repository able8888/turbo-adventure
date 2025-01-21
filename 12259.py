n=int(input())
a=input().split()
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]+a[j]<a[j]+a[i]:
            a[i],a[j]=a[j],a[i]
sum="".join(a)
a.reverse()
print(sum+" "+"".join(a))