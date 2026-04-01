class Solution: 
    def sortArray(self, nums: List[int]) -> List[int]: 
        for i in range(len(nums)):
            j=i+1 
            for j in range(len(nums)): 
                if(nums[j]>nums[i]): 
                    nums[i],nums[j]=nums[j],nums[i]
           
        return nums