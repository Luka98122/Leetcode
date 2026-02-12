hm = {}
class Solution:
    def fib(self, n: int) -> int:
        if n <=1: return n
        if n in hm.keys(): return hm[n]
        val = self.fib(n-1)+self.fib(n-2)
        hm[n] = val
        return val

c = Solution()
print(c.fib(4))