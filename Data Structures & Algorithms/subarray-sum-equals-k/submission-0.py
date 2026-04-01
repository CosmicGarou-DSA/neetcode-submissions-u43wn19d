class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        csum = 0
        prefixsums = {0: 1}
        
        for n in nums:
            csum += n
            
            diff = csum - k
            if diff in prefixsums:
                count += prefixsums[diff]
            
            prefixsums[csum] = prefixsums.get(csum, 0) + 1
            
        return count