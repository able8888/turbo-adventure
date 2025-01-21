n=int(input())
a,b,c,d=map(input().count,('1','2','3','4'))
if a>=c:
    print(d+b//2+c-(-(a-c+(b%2)*2)//4))
if a<c:
    print(d+b//2+a+c-a+b%2)



