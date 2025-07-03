n=5 
i=1 
while i<=n:
    print(i)
    i+=1 
    
def print1ton(i,n):
    #base case
    if i>n:
        return 
    #recursive case 
    print(i)
    print1ton(i+1,n) 
    
print1ton(1,10)    
        
        