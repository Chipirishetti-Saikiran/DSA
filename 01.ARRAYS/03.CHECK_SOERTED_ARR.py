#BRUTE FORCE

def sorted_Arr(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
arr=[1,2,3,4,5]
print(sorted_Arr(arr))                



#OPTIMAL
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  
