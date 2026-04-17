class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            c = nums[i] - 1
            if nums[i] != nums[c]:
                nums[i], nums[c] = nums[c], nums[i]
            else:
                i += 1
        for i in range(1,len(nums)+1):
            if i != nums[i-1]:
                return [nums[i-1],i]
        




        