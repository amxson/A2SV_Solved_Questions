class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dictt= {}
        for i in nums:
            dictt[i]=i
        arr = []
        for i in range(1,len(nums)+1):
            if i not in dictt:
                arr.append(i)
        return arr

        