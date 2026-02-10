class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for val,inn in enumerate(nums):
            if inn in hashmap:
                return[hashmap[inn],val]
            else:
                hashmap[target-inn] = val
        return -1
        
        
        
