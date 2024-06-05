class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1
        # For negative number
        elif n < 0 :
            return 1 / (x * self.myPow(x, -n - 1))
        # For even exponent
        elif n%2 ==0:
            half = self.myPow(x,n//2)
            return half * half
        # For odd exponent
        return x * self.myPow(x, n - 1)