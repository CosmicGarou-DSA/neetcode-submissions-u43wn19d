class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr=[]
        n=len(word1)
        m=len(word2)
        mlen=max(n,m)
        for i in range(mlen):
            if i<n:
                arr.append(word1[i])
            if i<m:
                arr.append(word2[i])
        merge=''.join(arr)
        return merge