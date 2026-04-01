class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        r=len(s)-1
        return len(s[r])