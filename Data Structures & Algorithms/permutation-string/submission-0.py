from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        n = len(s2)

        if size > n:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:size])

        if s1_count == window_count:
            return True

        l = 0
        for r in range(size, n):
            window_count[s2[r]] += 1
            window_count[s2[l]] -= 1
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]
            l += 1

            if window_count == s1_count:
                return True

        return False