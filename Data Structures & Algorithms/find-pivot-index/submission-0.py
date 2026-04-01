class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=0

        for i in range(len(nums)):
            if i==0:
                leftsum=0
            for j in range(i+1,len(nums)):
                rightsum+=nums[j]
            if leftsum==rightsum:
                return i
                break
            else:
                leftsum+=nums[i]
                rightsum=0
        return -1