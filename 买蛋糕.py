n=int(input())
if 1<=n<=5:
    expense=2*n
elif 6<=n<=10:
    expense=1.9*n
elif 11<=n<=15:
    expense=1.8*n
elif 16<=n<=20:
    expense=1.7*n
elif n>=21:
    expense=1.6*n
print(f'{expense:.2f}')