def sec_largest(arr):
    largest=sec_largest=float("-inf")# infinity = no space occpd in memory 
    for i in arr:
        if i>largest:
            sec_largest=largest
            largest=i 
        elif i>sec_largest and i!=largest:
            sec_largest=i 
    return sec_largest if sec_largest!=float("-inf") else -1
arr=[1,2,3,4,5,5]
print(sec_largest(arr))
#TC: O(n)
