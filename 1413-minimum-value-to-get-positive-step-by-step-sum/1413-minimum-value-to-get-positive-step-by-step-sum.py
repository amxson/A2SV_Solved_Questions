class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minn = float('inf')
        c = 0
        for i in nums:
            c+=i
            minn = min(minn,c)
        if minn<=0:
            return abs(minn)+1
        else: 
            return 1

        