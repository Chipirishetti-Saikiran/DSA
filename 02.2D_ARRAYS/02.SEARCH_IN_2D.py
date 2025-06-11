"""   
leetcode 74
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

"""

def Serach_ele_in_2D(arr,tar):
    for i in arr:
        for j in i:
            if j==tar:
                return True 
    return False 

arr=[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]        
    
tar=int(input())
print(Serach_ele_in_2D(arr,tar))    