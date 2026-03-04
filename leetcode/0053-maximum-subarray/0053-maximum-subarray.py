class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = 0
        maxx = float('-inf')
        for i in nums:
            c+=i
            maxx = max(maxx,c)
            if c<0:
                c=0
        return maxx

        