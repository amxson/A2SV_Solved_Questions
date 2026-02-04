class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left,right+1):
            cover = False
            for start,end in ranges:
                if  start <= x<=end:
                    cover = True
            if cover == False:
                return False

        return True    