class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i,j,k=0,1,2
        n=len(nums)
        arr=[]
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    w=nums[i]
                    x=nums[j]
                    y=nums[k]
                    z=-(w+x+y-target)
                    if z in nums[k+1:]:
                        quad=[w,x,y,z]
                        if quad not in arr:
                            arr.append(quad)
                    k+=1
                j+=1
            i+=1
        return arr