class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr2=[]
        product=1
        i,j=0,0;
        for i in range(len(nums)):
            j=i+1
            k=i-1
            if(i>0):
                while k>=0:
                    product*=nums[k]
                    k-=1
            while j<len(nums):
                product*=nums[j]
                j+=1
            arr2.append(product)
            product=1
        return arr2