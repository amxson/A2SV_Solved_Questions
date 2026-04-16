class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        doubles = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                doubles.append(abs(n))
            nums[abs(n)-1] *= -1
        return doubles

        