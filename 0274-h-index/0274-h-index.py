class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s = sorted(citations)
        n = len(s)
        maxx = 0

        for i in range(n):
            if s[i] <=len(s[i:]):
                maxx = max(maxx,s[i])
            else:
                maxx = max(maxx,len(s[i:]))
        return maxx