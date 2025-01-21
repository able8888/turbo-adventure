num = 1
while True:
    p, e, i, d = map(int, input().split())
    if [p, e, i, d] == [-1, -1, -1, -1 ]:
        break
    p %=23
    e %=28
    i %=33
    s = d+1
    while (s-p)%23 !=0 or (s-e)%28 !=0 or (s-i)%33 !=0:
        s +=1
    s -=d
    print(f'Case {num}: the next triple peak occurs in {s} days.')
    num +=1