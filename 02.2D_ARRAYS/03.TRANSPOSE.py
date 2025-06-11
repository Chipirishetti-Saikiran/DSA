matrix = [[1,2,3],[4,5,6],[7,8,9]]
m=len(matrix)
print(m)
n=len(matrix[0])
print(n)
res=[[0]*m for _ in range(n)]
print(res)
for i in range(m):
    for j in range(n):
        res[j][i]=matrix[i][j]
print(matrix)        
print(res)