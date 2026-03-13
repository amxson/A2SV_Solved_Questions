class Solution:
    def minOperations(self, nums: List[int]) -> int:
        t = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                continue
            else:
                if i<(len(nums)-2):
                    c =i
                    t+=1
                    for i in range(3):
                        if nums[c] == 0:
                            nums[c]=1
                        else:
                            nums[c]=0
                        c+=1
                else:
                    return -1
        return t
            
                        
