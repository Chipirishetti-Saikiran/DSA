class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        maps={}

        for i,val in enumerate(nums):
            remain_val=target-val 
            if remain_val in maps:
                return [maps[remain_val],i]
            maps[val]=i 
        return []             


        