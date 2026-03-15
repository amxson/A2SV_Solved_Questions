class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        x = target
        mv =0
        while maxDoubles >0 and x >1:
            if x%2==0:
                x = int(x/2)
                maxDoubles-=1
                mv+=1
            else:
                x-=1
                mv+=1
        mv+= x-1
        return mv