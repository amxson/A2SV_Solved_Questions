from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = ''
        sorts = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
        for i,j in sorts.items():
            ans+=i*j
        return ans



        