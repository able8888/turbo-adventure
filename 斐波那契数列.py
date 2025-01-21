n=int(input())
def fibonacci(n):
    if n==1 or n==2:
        result = 1
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
    return result
for i in range(n):
    i=int(input())
    print(fibonacci(i))