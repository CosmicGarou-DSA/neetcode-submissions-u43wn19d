class Solution:
    def maxDifference(self, s: str) -> int:
        count={}
        ss=list(s)
        for item in ss:
            count[item]=count.get(item,0)+1
        freq1=([v for v in count.values() if v%2==0])
        freq2=([v for v in count.values() if v%2!=0])
        if not freq1 and not freq2:
            return 0
        diff=[(odd-even) for odd in (freq2) for even in (freq1)]
        return max(diff)