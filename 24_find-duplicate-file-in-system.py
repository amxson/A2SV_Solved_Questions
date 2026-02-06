class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dictt = {}
        for i in paths:
            strs = i.split()
            x = strs[0]
            for i in range(1,len(strs)):
                y = strs[i].split("(")
                print(y)
                
                dictt.setdefault(y[1], []).append(f"{x}/{y[0]}")
        
        return[j for j in dictt.values() if len(j)>1] 
        


                



        