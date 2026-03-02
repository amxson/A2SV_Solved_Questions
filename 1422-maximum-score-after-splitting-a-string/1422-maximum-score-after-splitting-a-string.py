class Solution:
    def maxScore(self, s: str) -> int:
        m=0
        for i in s:
            m +=int(i)
        l = 0
        ans = 0
        for i in range(len(s)-1):
            if int(s[i])==0:
                l+=1
            else:
                m-=1
            ans = max(ans,l+m)
        return ans
            


        