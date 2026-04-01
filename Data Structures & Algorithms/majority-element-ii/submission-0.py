class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        n=len(nums)
        
        for item in nums:
            count[item]=count.get(item,0)+1
        maxvals=[k for k,v in count.items() if v>(n//3)]
        return maxvals