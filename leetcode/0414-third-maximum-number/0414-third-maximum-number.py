class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dictt = {}
        for i in nums:
            dictt[i] = i
        l = list(dictt.values())
        l.sort()
        print(l)
        if len(l)>=3:
            return l[-3]
        else:
            return l[-1]