class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total +=i
        c = 0
        par = 0
        for i in range(len(nums)-1):

            c+=nums[i]
            if (total -c-c)%2==0:
                par+=1
        return par


        