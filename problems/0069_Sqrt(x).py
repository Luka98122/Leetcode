class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = 2**16
        
        while lo <= hi:
            m = (lo + hi) // 2
            
            if m * m == x:
                return m
            elif m * m < x:
                lo = m + 1 
            else:
                hi = m - 1  
        
        return hi  