class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def is_palind(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return is_palind(l+1,r) or is_palind(l,r-1)
            l+=1
            r-=1

        return True