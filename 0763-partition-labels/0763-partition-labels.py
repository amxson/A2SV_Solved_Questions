class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ss = list(s)
        dictt = {}
        for i,h in enumerate(ss):
            dictt[h]=i
        h = 0
        res = []
        t = 0
        while h<len(ss):
            if ss[h]==dictt[ss[h]]:
                res.append(1)
                h+=1
            else:
                t = dictt[ss[h]]
                x  = 0
                i=h
                while i<len(ss) and  i<t:
                    if dictt[ss[i]]<=t:
                        i+=1
                        continue
                    else:
                        x = max(x,dictt[ss[i]])
                    if x>t:
                        t = x
                    i+=1
                res.append(t+1-h)
                h=t+1
        return res
                
                        
                    




        