
s=int(input())
maxmul=0
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
a=2
while a<=s-a:
    b = s - a
    if is_prime(a):
        if is_prime(b):
            c=a*b
            maxmul=max(maxmul,c)
            a+=1
            b=s-a
        else:
            a += 1
            b = s - a
    else:
        a += 1
        b = s - a

print(maxmul)

