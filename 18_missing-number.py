class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dictt = {}
        for i in nums:
            dictt[i]=i
        for i in range(len(nums)+1):
            if i not in dictt:
                return i


        