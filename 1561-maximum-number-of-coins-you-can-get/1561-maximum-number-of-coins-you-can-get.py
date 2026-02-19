class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        total = 0 
        m= n-2
        for i in range(len(piles)//3):
            total +=piles[m]
            m-=2
           
        return total

        