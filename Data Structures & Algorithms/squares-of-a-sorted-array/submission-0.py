class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            square=nums[i]**2
            arr.append(square)
            arr.sort()
        return arr