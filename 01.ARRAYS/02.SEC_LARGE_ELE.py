def Sec_lar_ele(arr):
    max_ele=Sec_max=float("-inf")
    for i in arr:
        if i>max_ele:
            Sec_max=max_ele 
            max_ele=i 
        else:
            if max_ele>i>Sec_max:
                Sec_max=i 
    return Sec_max

arr=[1,2,3,4,5]
print(Sec_lar_ele(arr))

                