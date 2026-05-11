from typing import List
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        This problem is the same as #3740, but the
        limit of the size of nums is increased from 
        100 -> 10^5.
        
        My original solution is optimal enough to work
        here too, no changes needed :)
        
        """
        
        hm = {}
        
        res = 2**31 # 101 is also safe according to the problem
        
        for i,num in enumerate(nums):
            if num in hm.keys():
                hm[num].append(i)
            else:
                hm[num] = [i]
        
        for key in hm.keys():
            if len(hm[key])>=3:
                for i in range(0,len(hm[key])-2):
                    r = abs(hm[key][i] - hm[key][i+1]) + \
                        abs(hm[key][i+1] - hm[key][i+2]) + \
                        abs(hm[key][i+2] - hm[key][i])
                    
                    res = min(res,r)
        
        if res == 2**31: return -1
        return res