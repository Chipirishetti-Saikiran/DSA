def intersection(arr1,arr2):
    m,n=len(arr1),len(arr2)
    res=[]
    if m>n:
        for i in arr1:
            if i in arr2 and i not in res:
                res.append(i)
    else:
        for j in arr2:
            for j in arr1 and j not in res:
                res.append(j)         
    return res               
    
arr1=[1,2,2,1]
arr2=[2,3,4]    
print(intersection(arr1,arr2))

    