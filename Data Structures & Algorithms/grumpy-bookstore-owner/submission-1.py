class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        Sum=maxsum=0
        satisfy=0

        for r in range(len(customers)):
            if grumpy[r]:
                Sum+=customers[r]
            else:
                satisfy+=customers[r]
            
            if r-l+1>minutes:
                if grumpy[l]:
                    Sum-=customers[l]
                l+=1

            maxsum=max(maxsum,Sum)

        return satisfy+maxsum