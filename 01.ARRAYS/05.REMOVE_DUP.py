def remove_dup(arr):
    uniq=[]
    for i in arr:
        if i not in uniq:
            uniq.append(i)
    return uniq 

arr=[1,1,2,2,3,3]
print(remove_dup(arr))

        