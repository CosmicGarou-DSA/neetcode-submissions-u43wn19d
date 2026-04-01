class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n_set=set(nums)
        longest=0

        for n in n_set:
            if n-1 not in n_set:
                count=1
                while n+count in n_set:
                    count+=1
                longest=max(longest,count)
        return longest
        