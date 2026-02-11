class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum = 0
        for i in nums:
            if i%2 == 0:
                sum+=i
        
        ans = []
        for val,ind in queries:
            x = nums[ind]
            nums[ind] += val
            if x%2 == 0 and val%2==0 :
                sum+=val
            elif x%2 != 0 and val%2!=0:
                sum+= nums[ind]
            elif x%2 == 0 and val%2!=0:
                sum-=x
            ans.append(sum)
        return ans
            
            

        