from collections import Counter
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        ans = []
        for i in dictionary:
            h = 0
            for j in s:
                if h< len(i) and i[h]==j:
                    h+=1
                
            if h == len(i):
                ans.append(i)
           
        anss = sorted(ans,key = lambda x: (-len(x),x))
        print(anss)
        return anss[0] if anss else ""
