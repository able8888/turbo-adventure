n=int(input())
a=list(map(int,input().split()))
def max_len(n,a):
    if n==1:
        print(1)
    else:
        up=1
        down=1
        for i in range(1,n):
            if a[i]>a[i-1]:
                up = down + 1
            elif a[i]<a[i-1]:
                down = up + 1
    return max(up,down)
print(max_len(n,a))

