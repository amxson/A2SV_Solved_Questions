class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        l, r = 1, max(candies)
        ans = 0
        
        while l <= r:
            m = (l + r) // 2
            c = 0
            for i in candies:
                c += i // m
            
            if c >= k:
                ans = m
                l = m + 1
            else:
                r = m - 1
        
        return ans



        