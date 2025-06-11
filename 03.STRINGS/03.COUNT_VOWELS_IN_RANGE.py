def count(words,left,right):
    vowels="aeiou"
    arr=words[left:right+1]
    count=0
    
    for i in arr:
        if i[0] in vowels and i[-1] in vowels:
            count+=1 
    print(count)        
    

words = ["hey","aeo","mu","ooo","artro"]
left = 1
right = 4
count(words,left,right)