A=int(input())
def bless(A):
    squares = set()
    i = 1
    while i * i<10**9:
        squares.add(i * i)
        i +=1
    list1=list(map(int,str(A)))
    def dfs(i):
        if len(list1) == i:
            return True
        num=0
        for i in range(i,len(list1)):
            num=num * 10 + list1[i]
            if num in squares:
                if dfs(i + 1):
                    return True
        return False
    return "Yes" if dfs(0) else "No"
print(bless(A))




