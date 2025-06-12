class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,j,k=0,0,len(nums)-1 
        arr=nums
        while j<=k:

            if arr[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1 

            elif arr[j]==1:
                j+=1 

            else:
                arr[j],arr[k]=arr[k],arr[j]
                k-=1 
        return  arr           

#leetcode 75 sort colors
        