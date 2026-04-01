class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss=s.split()
        map1={}
        map2={}

        if len(ss)>len(pattern) or len(ss)<len(pattern):
            return False

        for i in range(len(pattern)):
            ch1=pattern[i]
            ch2=ss[i]

            if ch1 in map1 and map1[ch1]!=ch2:
                return False
            if ch2 in map2 and map2[ch2]!=ch1:
                return False

            map1[ch1]=ch2
            map2[ch2]=ch1
        return True