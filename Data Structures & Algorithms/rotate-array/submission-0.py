class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       i,l=1,0
       n=len(nums)
       r=n-1
       arr=[]
       k=k%n
       while i<=k:
            arr.append(nums[r])
            arr.extend(nums[l:r])
            nums[:]=arr
            arr=[]
            i+=1
            