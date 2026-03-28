class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 2
        def dfs():
            nonlocal num
            if n ==1:
                return True
            if num == n:
                return True
            if num>n:
                return False
            num*=2
            return dfs()
        return(dfs())
        