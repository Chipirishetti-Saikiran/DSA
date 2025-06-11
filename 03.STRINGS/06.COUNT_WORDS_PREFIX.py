
def prefixCount(words, pref):
       
        n=len(pref)
        c=0 
        for i in words:
            if  i[:n]==pref:
                c+=1 
        return c
        

words = ["pay","attention","practice","attend"]
pref = "at"
print(prefixCount(words, pref))
print(sum(1 for i in words if i.startswith(pref))) #OPTIMAL