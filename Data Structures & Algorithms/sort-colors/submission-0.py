class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if(nums[j]<nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
                j+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        