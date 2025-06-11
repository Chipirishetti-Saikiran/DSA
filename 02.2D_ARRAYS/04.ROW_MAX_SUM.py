matrix = [[1,2,3],[4,5,6],[7,8,9]]

#Brute Force 
max_sum=sum(matrix[0])
for i in range(len(matrix)):
    cal=sum(matrix[i])
    if cal>max_sum:
        max_sum=cal 
print(matrix[i])    
print(max_sum)        

#OPTIMAL
def max_row_sum(matrix):
    return max(sum(row) for row in matrix)

print(max_row_sum(matrix))