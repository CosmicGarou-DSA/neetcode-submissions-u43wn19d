class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        longest=0
        maxc=0
        count={}
        for r,ch in enumerate(s):
            count[ch]=count.get(ch,0)+1
            maxc=max(maxc,count[ch])

            while (r-l+1)-maxc >k:
                count[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest