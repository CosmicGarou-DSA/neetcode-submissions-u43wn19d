class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        i=1

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[j]==target-nums[i]):
                    return[i+1,j+1]
                    break
                else:
                    j+=1
