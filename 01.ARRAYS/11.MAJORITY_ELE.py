
    def majorityElement(nums):

        for i in set(nums):
            if nums.count(i)>len(nums)//2:
                return i