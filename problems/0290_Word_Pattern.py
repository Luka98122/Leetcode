class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split(' ')
        
        if len(a)!=len(pattern): return False
        
        hm1 = {}
        
        for i,char in enumerate(pattern):
            if char not in hm1.keys():
                hm1[char]=a[i]
            else:
                if a[i]!=hm1[char]:
                    return False
            
        hm2 = {}
        for i, word in enumerate(a):
            if word not in hm2.keys():
                hm2[word]=pattern[i]
            else:
                if pattern[i]!=hm2[word]:
                    return False

        
        return True
        