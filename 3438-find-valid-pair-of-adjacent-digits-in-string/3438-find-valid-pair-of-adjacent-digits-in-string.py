from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        c = Counter(s)
        for i in range(len(s)-1):
            fir= s[i]
            sec= s[i+1]
            if fir!=sec and  int(fir) == int(c[fir]) and  int(sec) == int(c[sec]):
                return fir+sec
        
        return ''




        