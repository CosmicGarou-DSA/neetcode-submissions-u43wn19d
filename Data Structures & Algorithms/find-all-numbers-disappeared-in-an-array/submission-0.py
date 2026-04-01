class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            arr.append(i+1)
        disappear=[ch for ch in arr if ch not in nums]
        return disappear