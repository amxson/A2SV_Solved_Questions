from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
       a1,c1 = None,0
       a2,c2 = None,0
       ans = []
       for i in nums:
        if i==a1:
            c1+=1
        elif i == a2:
            c2+=1
        elif c1 == 0:
            a1 = i
            c1=1
        elif c2 == 0:
            a2 = i
            c2=1
        else:
            c1-=1
            c2-=1

       for i in [a1,a2]:
        if i is not None and nums.count(i)>len(nums)/3:
            ans.append(i)
       return list(set(ans))

