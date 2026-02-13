from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res = []
        for i in responses:
            res.extend(set(i))
        c = Counter(res)
        sorted_ = sorted(c.items(), key=lambda x: (-x[1], x[0]))

        
        return sorted_[0][0]


        