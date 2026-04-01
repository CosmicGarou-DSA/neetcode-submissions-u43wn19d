class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
    
    # Keep shrinking the window until it is size k
        while right - left + 1 > k:
        # Check which end is further from x
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
            
        return arr[left : right + 1]