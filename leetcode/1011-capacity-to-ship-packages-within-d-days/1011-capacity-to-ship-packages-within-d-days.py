class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(c):
            need = 1
            cw = 0

            for w in weights:
                if cw + w > c:
                    need += 1
                    cw = 0
                cw += w

            return need <= days

        l, r = max(weights), sum(weights)

        while l < r:
            mid = l + (r - l) // 2

            if canShip(mid):
                r = mid
            else:
                l = mid + 1

        return l