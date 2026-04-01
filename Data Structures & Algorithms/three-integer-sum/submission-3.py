class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        arr=set()
        while i<len(nums):
            j=i+1
            while j<len(nums):
                x=nums[i]
                y=nums[j]
                z=-(x+y)
                if z in nums[j+1:]:
                    arr.add(tuple(sorted([x,y,z])))
                j+=1
            i+=1
        
        return [list(t) for t in arr]