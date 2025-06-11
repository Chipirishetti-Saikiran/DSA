#BRUTE FORCE 
def rev(str):
    
    updated=""
    for i in s:
        #print(i)
        updated=i+updated 
    print(updated)
        
s = ["h","e","l","l","o"]    
rev(s)

#OPTIMAL 
def rev(str):
    i=0
    j=len(s)-1 
    while i<j:
        s[i],s[j]=s[j],s[i]
        i+=1 
        j-=1 
    return s 
    
s = ["h","e","l","l","o"]    
print(rev(s))
   