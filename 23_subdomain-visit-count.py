class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictt = {}
        ans = []
        for i in cpdomains:
            visit,domain = i.split()
            domain = domain.split('.')
            for j in range(len(domain)):
                newd = ".".join(domain[j:])
                dictt[newd] = dictt.get(newd,0)+int(visit)
        print(dictt)
        for dom,tvisit in dictt.items():
            ans.append(f"{tvisit} {dom}")
        return ans


            
        

        