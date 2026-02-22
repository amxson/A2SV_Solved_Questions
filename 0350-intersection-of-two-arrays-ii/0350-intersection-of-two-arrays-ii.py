from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = Counter(nums1)
        arr = []
        for i in nums2:
            if i in x:
                x[i]-=1
                arr.append(i)
            if x[i]==0:
                del x[i]
        return arr
        
        
        