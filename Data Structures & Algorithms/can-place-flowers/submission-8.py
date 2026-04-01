class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        for i in range(len(flowerbed)):
            if (flowerbed[i]==0):
                lplot=(i==0) or (flowerbed[i-1]==0)
                rplot=(i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if lplot and rplot:
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                        return True
        return n<=0