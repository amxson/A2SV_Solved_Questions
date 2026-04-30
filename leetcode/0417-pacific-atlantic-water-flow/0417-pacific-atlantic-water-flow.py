
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)

            directions = [
                (1, 0),  
                (-1, 0),  
                (0, 1),  
                (0, -1)   
            ]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                   
                    if (nr, nc) in visited:
                        continue

                    
                    if heights[nr][nc] < heights[r][c]:
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))

            return visited

        pacific_starts = []
        atlantic_starts = []

       
        for r in range(rows):
            pacific_starts.append((r, 0))        
            atlantic_starts.append((r, cols - 1)) 

        for c in range(cols):
            pacific_starts.append((0, c))         
            atlantic_starts.append((rows - 1, c)) 

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result