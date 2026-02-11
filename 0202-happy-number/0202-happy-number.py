class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        while n !=1 and n not in sett:
            sett.add(n)
            y = 0
            while n!= 0:
                d=n%10
                n=n//10
                y+= d**2
            n = y
            
        return n==1

            

        