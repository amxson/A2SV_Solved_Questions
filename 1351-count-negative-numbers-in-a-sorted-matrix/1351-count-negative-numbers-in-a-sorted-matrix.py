class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        r,c = len(grid),len(grid[0])
        rr,cc = r-1 ,0
        while rr>=0 and cc<c:
            if grid[rr][cc]<0:
                count+=(c-cc)
                rr-=1
            else:
                cc+=1
        return count

        