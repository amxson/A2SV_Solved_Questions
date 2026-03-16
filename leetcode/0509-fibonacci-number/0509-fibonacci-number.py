class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1

        
        def fibo(a, b, count):
            if count == n:
                return b
            return fibo(b, a + b, count + 1)

        return fibo(0, 1, 1) 
    

        