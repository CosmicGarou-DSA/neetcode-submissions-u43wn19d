class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]',"",s).lower()
        arr=list(s)
        i=0
        j=len(arr)-1
        while i<j:
            if(arr[i]==arr[j]):
                 i+=1
                 j-=1
            else:
                return False
        return True
        