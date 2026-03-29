class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        sett = set()
        def dfs():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in sett:
                    continue
                path.append(nums[i])
                sett.add(nums[i])
                dfs()
                path.pop()
                sett.remove(nums[i])
        dfs()
        return ans
        