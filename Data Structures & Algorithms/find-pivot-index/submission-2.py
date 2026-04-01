class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=0
        totalsum=sum(nums)
        for i in range(len(nums)):
            if i==0:
                leftsum=0
            rightsum=totalsum-leftsum-nums[i]
            if leftsum==rightsum:
                return i
                break
            else:
                leftsum+=nums[i]
                rightsum=0
        return -1