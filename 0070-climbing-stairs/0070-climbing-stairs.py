class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        f1=2
        f2=1
        for i in range(3,n+1):
            curr=f1+f2
            f2=f1
            f1=curr
        return f1