class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    arr.append(words[i])
        sarr=set(arr)
        ssarr=list(sarr)
        return ssarr