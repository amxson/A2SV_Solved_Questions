class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = ''.join(map(str,nums))
        print(s)
        ans = []
        for i in s:
            ans.append(i)
        return list(map(int,ans))