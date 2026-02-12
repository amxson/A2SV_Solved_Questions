class Solution:
    def imageSmoother(self, img):
        rows = len(img)
        cols = len(img[0])

        ans = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                total = 0
                count = 0

                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            total += img[nr][nc]
                            count += 1

                ans[r][c] = total // count

        return ans
