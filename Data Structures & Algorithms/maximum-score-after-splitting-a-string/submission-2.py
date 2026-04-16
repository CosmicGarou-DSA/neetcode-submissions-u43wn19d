class Solution:
    def maxScore(self, s: str) -> int:
        maxsum=0
        n=len(s)
        for i in range(n-1):
            left=(s[0:i+1]).count('0')
            right=(s[i+1:n]).count('1')
            maxsum=max(maxsum,(right+left))
        return maxsum