class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        h = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[h],nums[i]=nums[i],nums[h]
                h+=1
                
            
        """
        Do not return anything, modify nums in-place instead.
        """
        