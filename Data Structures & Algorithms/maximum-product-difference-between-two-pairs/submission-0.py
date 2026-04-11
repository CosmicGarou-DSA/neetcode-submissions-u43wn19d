class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        sort=sorted(nums)

        return ((sort[j]*sort[j-1])-(sort[i]*sort[i+1]))
        