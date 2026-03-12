class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = 0
        for i in range(len(nums)):
            if i> maxx:
                return False
            maxx = max(maxx,i+nums[i])
            if maxx>=(len(nums)-1):
                return True
        return False
        