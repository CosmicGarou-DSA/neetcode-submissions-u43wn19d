class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m=-1
        for i in range(len(arr)-1,-1,-1):
            cvalue=arr[i]

            arr[i]=m

            if cvalue>m:
                m=cvalue

        return arr