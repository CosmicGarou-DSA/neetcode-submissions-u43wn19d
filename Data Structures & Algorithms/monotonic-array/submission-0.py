class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc=True
        dec=True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                inc=False
                break
            
        if inc:
            return True

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dec=False
                break

        return dec