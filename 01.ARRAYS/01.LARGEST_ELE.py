def Largest_ele(arr):
    max_ele=arr[0]
    for i in arr:
        if i>max_ele:
            max_ele=i 
    return max_ele 

arr=[1,5,3,8,12]
print(Largest_ele(arr))        