class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter(nums)
        i=0
        n=len(nums)
        pairs=n/2
        while i<len(count) and count[i]%2==0:
            i+=1
        if i==len(count):
            return True
        else:
            return False