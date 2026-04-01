class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        Sum=0
        maxSum=0
        for i in range(len(nums)):
            if i==0 or nums[i-1]<nums[i]:
                Sum+=nums[i]
                maxSum=max(maxSum,Sum)
            elif nums[i-1]>=nums[i]:
                Sum=nums[i]
        return maxSum