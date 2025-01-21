n=int(input())
p,q=map(int,input().split())
numbers=[]
for _ in range(n):
    l,r=map(int,input().split())
    numbers.append([l,r])
numbers.sort(key=lambda x:(x[0]*x[1]))
maxgold=0
for i in range(n):
    maxgold=max(maxgold,p//numbers[i][1])
    p*=numbers[i][0]
print(maxgold)


