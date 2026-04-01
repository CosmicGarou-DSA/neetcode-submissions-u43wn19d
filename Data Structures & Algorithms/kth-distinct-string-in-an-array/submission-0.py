class Solution:
    def kthDistinct(self, arr: List[str], d: int) -> str:
        count={}
        for item in arr:
            count[item]=count.get(item,0)+1
        distinct=[item for item in arr if count[item]==1]
        if len(distinct)>=d:
            return distinct[d-1]
        else:
            return ""