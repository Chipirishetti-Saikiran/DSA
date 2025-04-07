def largest_Ele(arr):
    max_ele=arr[0]
    for i in arr:
        if i>max_ele:
            max_ele=i 
    return max_ele 
arr=[1,2,3,10,4]
print(largest_Ele(arr))
#TC: O(n)
