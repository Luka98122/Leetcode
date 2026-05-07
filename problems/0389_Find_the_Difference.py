from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s=="": return t
        if t=="": return s
        
        a = defaultdict(int)
        b = defaultdict(int)
        
        for char in s:
            a[char]+=1
        
        for char in t:
            b[char]+=1
        
        
        for key in b.keys():
            if not key in a.keys(): return key
            
            if a[key]!=b[key]: return key
    
c = Solution()
print(c.findTheDifference("abc","abcd"))