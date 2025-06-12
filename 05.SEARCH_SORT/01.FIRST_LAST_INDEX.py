def first_last(arr,tar):
    first = -1
    last = -1

    # Find first occurrence
    for i in range(len(arr)):
        if arr[i] == tar:
            first = i
            break

    # Find last occurrence (only if first was found)
    if first != -1:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == tar:
                last = i
                break

    return [first, last]
nums = [5,7,7,8,8,10]
target = 8   
print(first_last(nums,target))
#op:[3,4]



#OPTIMAL
def find_first_last(arr, target):
    def find_index(find_first):
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                if find_first:
                    high = mid - 1  # Keep searching left
                else:
                    low = mid + 1   # Keep searching right
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    first = find_index(True)
    last = find_index(False)
    return [first, last]

# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(find_first_last(nums, target))  # Output: [3, 4]

target = 6
print(find_first_last(nums, target))  # Output: [-1, -1]
