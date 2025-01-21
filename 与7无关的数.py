n=int(input())
a=[]
def f(i):
    while i>0:
        b=i%10
        if b==7:
            return False
        else:
            i=i//10
    return True
for i in range(1,n+1):
    if i%7==0:
        continue
    elif f(i):
        a.append(i)
print(sum(x**2 for x in a))