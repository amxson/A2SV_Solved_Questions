class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dictt =  defaultdict(int)
        dictt[0]=1
        pre  = 0
        ans = 0
        for i in nums:
            pre+=i
            ans+=dictt[pre%k] 
            dictt[pre%k]+=1
        return ans