class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count={}
        m=len(magazine)
        countrn=Counter(ransomNote)
        countmg=Counter(magazine)

        for ch in countrn:
            if countmg[ch]<countrn[ch]:
                return False
        return True