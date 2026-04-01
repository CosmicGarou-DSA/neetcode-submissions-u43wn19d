class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        i=0
        A=sorted(nums)
        n=len(A)
        for x in[i for i,val in enumerate(A) if val==nums[0]]:
            while i<n and nums[i]==A[(i+x)%n]:
                i+=1
        if i==n:
            return True
        return False
    