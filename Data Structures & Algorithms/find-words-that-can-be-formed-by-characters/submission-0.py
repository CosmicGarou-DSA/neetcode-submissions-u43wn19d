class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=Counter(chars)
        length=0

        for w in words:
            countword=Counter(w)
            flag=True
            for ch in countword:
                if countword[ch]>count[ch]:
                    flag=False
                    break
            if flag:
                length+=len(w)

        return length
            