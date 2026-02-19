class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = len(points)
        i = 0
        
        while i<len(points):
            j=i+1
            minn = points[i][1]
            while j < len(points) and points[j][0]<=minn:
                    count-=1
                    minn = min(minn,points[j][1])
                    j+=1
            i=j
            
        return count


        