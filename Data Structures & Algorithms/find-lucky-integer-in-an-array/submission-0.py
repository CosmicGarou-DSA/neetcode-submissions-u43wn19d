class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count={}

        for item in arr:
            count[item]=count.get(item,0)+1
        
        lucky=[k for k,v in count.items() if v==k]
        if not lucky:
            return -1
        else:
            return max(lucky)