n=5 
while n>0:
    print(n)
    n-=1 
    
def printnto1(n,i):
    #base case
    if n<i:
        return     
    # recursive case 
    print(n)
    printnto1(n-1,i)
printnto1(5,2)    