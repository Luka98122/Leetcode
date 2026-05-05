from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm1 = {}
        hm2 = {}

        for i,item in enumerate(list1):
            if item in hm1.keys():
                continue
            hm1[item]=i
        
        for i,item in enumerate(list2):
            if item in hm2.keys():
                continue
            hm2[item]=i
        
        best_found=2002 # From the problem constraints
        ans = []
        for key in hm1.keys():
            if key in hm2.keys():
                if (hm1[key]+hm2[key]<best_found):
                    best_found = hm1[key]+hm2[key]
                    ans = [key]
                else:
                    if (hm1[key]+hm2[key]==best_found):
                        ans.append(key)
        
        return ans