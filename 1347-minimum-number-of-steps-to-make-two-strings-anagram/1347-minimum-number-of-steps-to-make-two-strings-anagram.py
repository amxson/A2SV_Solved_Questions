from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ss = Counter(s)
        tt = Counter(t)
        count = 0
        for char in ss:
            if ss[char]>tt[char]:
                count += ss[char]-tt[char]
        return count
        

        