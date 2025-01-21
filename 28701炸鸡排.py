n,k = map(int,input().split())
t = list(map(int,input().split()))
t.sort()
s=sum(t)
while True:
    if s/k < t[-1]:
        k -= 1
        s -= t.pop()
    else:
        print(f'{s/k:.3f}')
        break




