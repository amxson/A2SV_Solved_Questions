class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for x in range(n):
            if(x>0 and nums[x] == nums[x-1]):
                continue
            for y in range(x+1,n):
                if(y>x+1 and nums[y]== nums[y-1]):
                    continue
                l = y+1
                r = n-1
                while(l<r):
                    t = nums[x]+nums[y]+nums[l]+nums[r]
                    if(t<target):
                        l += 1
                    elif(t>target):
                         r -=1
                    else:
                        ans.append([nums[x],nums[y],nums[l],nums[r]])
                        while(l<r and nums[l] == nums[l+1]):
                            l +=1
                        while(l<r and nums[r] == nums[r-1]):
                            r -=1
                        l +=1
                        r -= 1
        return ans


        