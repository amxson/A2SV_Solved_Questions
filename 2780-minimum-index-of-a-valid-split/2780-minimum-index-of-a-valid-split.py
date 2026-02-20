from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n= len(nums)
        freq = Counter(nums)
        dominant = None
        total = 0
        
        for num, count in freq.items():
            if count * 2 > n:
                dominant = num
                total = count
                break
        lc=0
        for i in range(n - 1):
            if nums[i] == dominant:
                lc += 1
            
            l = i + 1
            r = n - l
            rc = total - lc
            
            
            if lc * 2 > l and rc * 2 > r:
                return i
        
        return -1


        
        