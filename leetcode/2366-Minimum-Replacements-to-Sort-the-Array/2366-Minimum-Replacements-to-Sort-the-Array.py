import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans  = 0
        l = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if l<nums[i]:   
                p = math.ceil(nums[i]/l)
                ans +=p-1
                l = nums[i]//p
                continue
            l = nums[i]
        return ans