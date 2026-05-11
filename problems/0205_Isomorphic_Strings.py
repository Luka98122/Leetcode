from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #mapping s -> t
        hm = {}
        for i in range(len(s)):
            if s[i] in hm.keys():
                hm[s[i]].append(t[i])
            else:
                hm[s[i]] = [t[i]]
        
        for key in hm.keys():
            if len(set(hm[key]))>1: # 1 key maps to two different values
                return False
        
        # Check mapping t -> s
        hm = {}
        for i in range(len(t)):
            if t[i] in hm.keys():
                hm[t[i]].append(s[i])
            else:
                hm[t[i]] = [s[i]]
        
        for key in hm.keys():
            if len(set(hm[key]))>1:
                return False

        return True