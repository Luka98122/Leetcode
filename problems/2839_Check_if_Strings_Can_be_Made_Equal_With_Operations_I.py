class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        # Simple but works. 
        
        if not s1 or not s2: return False
        
        if s1==s2: return True
        
        perms = []
        s = list(s2)
        
        r1 = s[0]+s[3]+s[2]+s[1]
        r2 = s[2]+s[3]+s[0]+s[1]
        
        r3 = s[2]+s[1]+s[0]+s[3]
        
        return s1==r1 or s1==r2 or s1==r3