class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        sum=0
        length=float('inf')
        n=len(nums)

        for r in range(n):
            sum+=nums[r]
            r+=1

            while sum>=target:
                sum-=nums[l]
                l+=1
                length=min(length,r-l+1)

        return length if length<=n else 0