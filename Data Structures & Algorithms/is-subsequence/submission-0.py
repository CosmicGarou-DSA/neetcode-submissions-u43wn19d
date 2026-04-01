class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        arr=[]
        s1=[c for c in s]
        s2=[c for c in t]
        m=len(s1)
        n=len(s2)
        while i < m and j < n:
                if s1[i]==s2[j]:
                    i+=1
                j+=1
        if i==m:
            return True
        else:
            return False


        