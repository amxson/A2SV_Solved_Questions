class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = 1
        cc = 1
        ans = []
        ccc= 0
        for i in nums:
            c*=i
            if i!=0:
                cc*=i
            if i==0:
                ccc+=1
        if ccc>1:
            cc=c
            
            
        for i in range(len(nums)):
            if nums[i]!=0:
                ans.append(int(c/nums[i]))
            else:
                ans.append(cc)
        return ans

        