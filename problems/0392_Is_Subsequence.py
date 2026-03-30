class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        b = 0
        n = len(s)
        m = len(t)

        while a<n and b<m:
            if s[a]==t[b]:
                a+=1
            
            b+=1
        
        if a==n:
            return True
        return False
    
c = Solution()
print(c.isSubsequence("ace","abcde"))