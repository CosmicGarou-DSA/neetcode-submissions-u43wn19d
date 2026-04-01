class Solution:
    def maxArea(self, heights: List[int]) -> int:
        arr=[]
        p=1
        l,r=0,len(heights)-1
        while l<r:
            p=(r-l)*min(heights[l],heights[r])
            arr.append(p)
            p=1
            if( heights[l]<heights[r]):
                l+=1
            elif (heights[l]>heights[r] or heights[l]==heights[r]):
                r-=1
        maxwater=max(arr)
        return maxwater