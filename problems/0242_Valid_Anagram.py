class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        
        abc = "abcdefghijklmnopqrstuvwxyz"
        for c in abc:
            hm1[c] = 0
            hm2[c] = 0
            
        for c in s:
            hm1[c]+=1
        for c in t:
            hm2[c]+=1
        
        for c in abc:
            if hm1[c] != hm2[c]: return False
        return True
