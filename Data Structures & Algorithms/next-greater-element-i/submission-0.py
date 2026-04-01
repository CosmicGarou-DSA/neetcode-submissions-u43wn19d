class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for n in nums1:
            j=nums2.index(n)
            nextg=-1
            for k in range(j+1,len(nums2)):
                if nums2[k]>n:
                    nextg=nums2[k]
                    break
            arr.append(nextg)
                    
        return arr