class Solution:
    def fib(self, n: int) -> int:
        f,s, = 0, 1
        ans = 0
        if n == 0: return f
        if n == 1: return s
        def fibo(f ,s):
            return s, f+s
            

        while n >1:
            f,s = fibo(f,s)
            n-=1
        return s
    

        