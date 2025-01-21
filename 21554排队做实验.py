n=int(input())
time=list(map(int,input().split()))
students=sorted(enumerate(time,start=1),key=lambda x: x[1])
order=[student[0] for student in students]
sorted_time=[student[1] for student in students]
total_time=0
current_time=0
for t in sorted_time:
    total_time+=current_time
    current_time+=t
average_time=total_time/n
print(" ".join(map(str,order)))
print(f'{average_time:.2f}')
