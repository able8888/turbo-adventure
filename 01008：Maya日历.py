n=int(input())
Haab={"pop":1, "no":2,"zip":3, "zotz":4, "tzec":5, "xul":6, "yoxkin":7, "mol":8, "chen":9, "yax":10, "zac":11, "ceh":12, "mac":13, "kankin":14, "muan":15, "pax":16, "koyab":17, "cumhu":18,"uayet":19}
Tzolkin={1:"imix",2:"ik",3:"akbal",4:"kan",5:"chicchan",6:"cimi",7:"manik",8:"lamat",9:"muluk",10:"ok",11:"chuen",12:"eb",13:"ben",14:"ix",15:"mem",16:"cib",17:"caban",18:"eznab",19:"canac",20:"ahau"}
print(n)
for _ in range(n):
    day,month,year=input().split()
    day=int(day.rstrip("."))
    total=(Haab[month]*20+day+1+(year-1)*365)//260
