from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        y = x.most_common(k)
        result = [num for num, freq in y]
        return result  

        