def Sprial(arr):
    res=[]
    while arr:
        #STEP1=> fetch 1st row and add to res
        k=arr.pop(0)
        #print(k)
        res+=k 
        #print(res)
        #print(arr)
        
        #Now arr => [ [4,5,6],[7,8,9]]
        
        #STEP 2=> fetch last element in each row and add to res 
        if arr and arr[0]:
            for i in arr:
                last_ele=i.pop()
                #print(last_ele)
                res.append(last_ele)
        #print(res)    
        
        #Now arr => [ [4,5],[7,8]]
        
        #STEP 3=> fetch last row  and add ele in reverse to res 
        
        if arr:
             bottom_row = arr.pop()                  
             bottom_row_reversed = bottom_row[::-1] 
             for element in bottom_row_reversed:
                res.append(element) 
        #print(res)    
       
        #Now arr => [[4,5]]
        
       
        
        if arr and arr[0]:
            for row in reversed(arr):
                res.append(row.pop(0))        
    print(res)            

mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
Sprial(mat)    