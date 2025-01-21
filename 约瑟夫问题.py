while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    data = []
    deldata = []
    for i in range(1,n+1):
        data.append(i)
    num=0
    while len(data)>1:
        num+=1
        temp=data.pop(0)#可以改成deque内置函数
        if num==m:
            deldata.append(temp)
            num=0
        else:
            data.append(temp)
    print(data[0])




