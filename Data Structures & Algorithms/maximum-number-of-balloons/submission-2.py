class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ogcount=Counter('balloon')
        count=Counter(text)

        maxcount=len(text)
        for ch in 'balloon':
            maxcount=min(maxcount,count[ch]//ogcount[ch])
        return maxcount 
        