class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_max=nums[0]
        initial_max=nums[0]
        for i in nums[1:]:
        
            initial_max=max(initial_max+i,i)
            final_max=max(final_max,initial_max)
        return final_max 
    
#KADANES ALGORITHM    