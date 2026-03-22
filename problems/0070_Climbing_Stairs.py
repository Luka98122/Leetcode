class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1,2]
        
        for i in range(2,46): # max n=45
            fib.append(fib[i-1]+fib[i-2])
        return fib[n-1]

c = Solution()
print(c.climbStairs(2))
print(c.climbStairs(3))
