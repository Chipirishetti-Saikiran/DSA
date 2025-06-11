def move_zeros(arr):
    n=len(arr)
    non_zero=[i for i in arr if i!=0]
    zero=[0]*(n-len(non_zero))
    return non_zero+zero

#Optimal

        pos = 0  # Position to place the next non-zero element

        # 1st pass: Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # 2nd pass: Fill remaining positions with 0
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
arr=[0,1,0,12,0,13]
print(move_zeros(arr))

