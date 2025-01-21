def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
while True:
    try:
        n,m=map(int,input().split())
    except:
        break
    print(gcd(n,m))