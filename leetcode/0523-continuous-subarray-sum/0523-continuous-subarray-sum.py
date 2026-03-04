class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        c = {0: -1}
        d = 0
        
        for i, num in enumerate(nums):
            d += num
            rem = d % k
            
            if rem in c:
                if i - c[rem] >= 2:
                    return True
            else:
                c[rem] = i
        
        return False
