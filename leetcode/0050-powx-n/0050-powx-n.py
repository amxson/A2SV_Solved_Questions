class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n<0:
                n*=-1
                x =1/x
            if n ==0:
                return 1.0
            half = power(x,n//2)
            ans =1
            if n%2!=0:
                ans*=x
            ans *= half *half
            return ans
        return(power(x,n))



            
            
        
       



        