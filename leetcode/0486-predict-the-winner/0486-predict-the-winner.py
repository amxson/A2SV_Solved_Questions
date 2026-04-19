class Solution:
    def predictTheWinner(self, nums):
        def dfs(l, r):
            if l == r:
                return nums[l]
            a = nums[l] - dfs(l + 1, r)
            b = nums[r] - dfs(l, r - 1)
            return max(a, b)

        return dfs(0, len(nums) - 1) >= 0