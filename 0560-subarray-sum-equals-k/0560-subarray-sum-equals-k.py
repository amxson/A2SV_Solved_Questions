class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        t = 0
        s = 0
        pre = {0:1}
        for i in range(len(nums)):
            t+= nums[i]
            s+= pre.get(t-k,0)
            pre[t] = pre.get(t,0)+1 
        return s



        