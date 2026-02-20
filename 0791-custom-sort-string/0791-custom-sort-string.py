class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def custom(s):
            if s in order:
                pos = order.index(s)
                return pos
            else:
                return len(order)+10
        return(''.join(sorted(s,key=custom)))

        