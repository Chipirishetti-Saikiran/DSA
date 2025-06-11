def Matrix(arr,m,n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j],end=" ")
        print(" ")
        
m=n=3 
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]     
Matrix(arr,m,n)