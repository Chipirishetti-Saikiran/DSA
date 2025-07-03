def Is_Prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True  

     
def Count_Prime(n):
    c=0 
    for i in range(2,n+1):
        if Is_Prime(i):
            c+=1 
    print(c)

n=int(input())
Count_Prime(n)


