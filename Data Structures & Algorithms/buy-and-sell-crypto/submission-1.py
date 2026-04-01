class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitarr=[]
        profit=0
        i,j=0,0
        while i<len(prices):
            j=i+1
            while j<len(prices):
                if(prices[j]>prices[i] or prices[j]==prices[i]):
                    profit=prices[j]-prices[i]
                    profitarr.append(profit)
                    profit=0
                    j+=1
                elif(prices[j]<prices[i]):
                    j+=1
                else:
                    i+=1
            i+=1
            j=0
        if not profitarr:
            return 0
        else:
            return max(profitarr)