class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        zero = 0
        sett = defaultdict(int)
        for i in answers:
            sett[i]+=1

        t= 0
        for i,j in sett.items():
                if i == 0:
                    t+=sett[i]
                else:
                    x = sett[i]
                    while x>i+1:
                        t+= i+1
                        x-=i+1
                    t+=i+1
        return t

        