class Solution:
    def scoreOfString(self, s: str) -> int:
        arr=[ord(c) for c in s]
        i=0
        score=0
        last=len(arr)-1
        while i<last :
            diff=abs(arr[i+1]-arr[i])
            score+=diff
            i+=1
        return score
