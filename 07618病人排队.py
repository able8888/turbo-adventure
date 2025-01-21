n=int(input())
elderly=[]
non_elderly=[]
for _ in range(n):
    patientID,age=input().split()
    age=int(age)
    if age>=60:
        elderly.append((patientID,age))
    else:
        non_elderly.append((patientID,age))
elderly.sort(key=lambda x:-x[1])

sum_patient=elderly+non_elderly
for i in sum_patient:
    print(i[0])