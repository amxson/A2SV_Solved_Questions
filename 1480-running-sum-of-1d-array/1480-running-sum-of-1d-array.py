class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans = [0]*n
        t = 0
        for i in range(n):
            t +=nums[i]
            ans[i]=t
        return ans
        