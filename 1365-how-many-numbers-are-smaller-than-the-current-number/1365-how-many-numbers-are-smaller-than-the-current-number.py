class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        f = nums.copy()
        f.sort()
        dictt = {}
        c = 0
        for i in range(len(f)):

            if i == 0:
                dictt[f[i]] = c
            if f[i]==f[i-1]:
                dictt[f[i]]= c
            else:
                c= i
                dictt[f[i]]=c
        for i in range(len(nums)):
            nums[i]= dictt[nums[i]]
        return nums
                



        