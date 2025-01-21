
n = int(input())
list_1 =[]

for i in range(n):
    a, b, c = map(int, input().split())
    list_1.append((i+1,a+b+c,a))
list_2=sorted(list_1,key=lambda x : (-x[1],-x[2],x[0]))

for i in range(5):
    print(list_2[i][0],list_2[i][1])