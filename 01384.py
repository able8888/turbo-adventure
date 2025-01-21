INF = float("inf")
T=int(input())
for _ in range(T):
    E,F=map(int,input().split())
    weight=F-E
    N=int(input())
    dp=[0]+[INF]*weight
    weight_list=[]
    for _ in range(N):
        P,W=map(int,input().split())
        weight_list.append((P,W))
    for i in range(N):
        p,w=weight_list[i]
        for j in range(w,weight+1):
            if dp[j-w]!=INF:
                dp[j]=min(dp[j],dp[j-w]+p)
    if dp[-1]!=INF:
        print(f'The minimum amount of money in the piggy-bank is {dp[-1]}.')
    else:
        print(f'This is impossible.')
