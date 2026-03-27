class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(start):
            ans.append(path[:])
            for j in range(start,len(nums)):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans




        