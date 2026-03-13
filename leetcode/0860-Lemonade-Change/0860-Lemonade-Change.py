class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = []
        c10 = []
        for i in bills:
            if i ==5:
                c5.append(i)
            elif i ==10:
                c10.append(i)
                if c5:
                    c5.pop()
                else:
                    return False
            else:
                x = 15 
                if c10:
                    c10.pop()
                    x-=10
                while x !=0:
                    if c5:
                        c5.pop()
                        x-=5
                    else:
                        return False 
        return True