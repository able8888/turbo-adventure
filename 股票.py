prices =[7,1,5,3,6,4]
i=0
j=1
profit=0
while j <= len(prices)-1 and i <= len(prices)-1:
    if prices[i]<prices[j]:
        profit +=prices[j] - prices[i]
        i = j
        j +=1
    else:
        i = j
        j += 1

print(profit)