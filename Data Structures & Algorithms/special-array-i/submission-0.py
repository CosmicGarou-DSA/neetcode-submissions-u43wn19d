class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def is_even(n):
            return n%2==0
        def is_odd(n):
            return n%2!=0
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if is_even(nums[i]) and is_even(nums[j]):
                    return False
                if is_odd(nums[i]) and is_odd(nums[j]):
                    return False
                i+=1
                j+=1
        return True
