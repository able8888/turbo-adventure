a=list(map(int,input().split()))
minprice=a[0]
maxvalue=0
for i in range(len(a)):
    if a[i]<minprice:
        minprice=a[i]
    else:
        maxvalue=max(a[i]-minprice,maxvalue)
print(maxvalue)

