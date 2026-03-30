from collections import defaultdict
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)

        hm3 = defaultdict(int)
        hm4 = defaultdict(int)
        
        for i in range(len(s1)):
            if i%2==0:
                hm1[s1[i]]+=1
                hm3[s2[i]]+=1
                
            else:
                hm2[s1[i]]+=1
                hm4[s2[i]]+=1
        
        if (hm1 == hm3 and hm2==hm4): return True
        return False
    
c = Solution()
print(c.checkStrings("abe", "bea"))
                