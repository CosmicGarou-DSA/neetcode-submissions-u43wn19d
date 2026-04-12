class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count,i=0,0
        largest=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                numst=(num[i]*3)
                if numst>largest:
                    largest=numst

        if largest!=0:
            return largest
        else:
            return ""
            