class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums=[]
        count={}
        n=len(grid)
        flat=[val for row in grid for val in row]
        for val in flat:
            count[val]=count.get(val,0)+1
            if count[val]>1:
                nums.append(val)
        for i in range(1,n**2+1):
            if i not in flat:
                nums.append(i)
        return nums