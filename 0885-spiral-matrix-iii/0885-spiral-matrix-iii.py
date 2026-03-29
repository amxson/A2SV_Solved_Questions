class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []

        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        
        
        result.append([rStart, cStart])

        steps = 1  

        while True:
            for i in range(4):
                dr, dc = directions[i]

                
                for _ in range(steps):
                    rStart += dr
                    cStart += dc

                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])

                    if len(result) == rows * cols:
                        return result

                #   
                if i % 2 == 1:
                    steps += 1

        return result

        