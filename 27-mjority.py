from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = len(nums)//3
        ans = []
        y = Counter(nums)
        for key,val in y.items():
            if val>x:
                ans.append(key)
        return ans