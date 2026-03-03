class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxx =0
        maxxx= 0
        c = defaultdict(int)
        for i in range(len(s)):
            c[s[i]]+=1
            maxxx = max(maxxx,c[s[i]])
            while (i-l+1)-maxxx>k:
                c[s[l]]-=1
                l+=1

                
            maxx  = max(maxx,i-l+1)
        return maxx



            
            

