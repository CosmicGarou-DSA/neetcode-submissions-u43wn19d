class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       n=len(nums)
       k=k%n
       arr=[]

       arr=nums[-k:]+nums[:-k]
       nums[:]=arr