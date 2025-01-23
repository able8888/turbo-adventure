N=int(input())
a=list(map(int,input().split()))
dp=[0]*N
dp[0]=a[0]
for i in range(N):
    dp[i]=a[i]
    for j in range(i):
        if a[j]<a[i]:
            dp[i]=max(a[i]+dp[j],dp[i])
print(max(dp))
