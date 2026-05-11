from typing import List
from collections import defaultdict
class Solution: #FT S5
    def findLHS(self, nums: List[int]) -> int:
        a = defaultdict(int) # Occurence count of unique nums
        
        for num in nums:
            a[num]+=1
        
        keys = sorted(a.keys())
        
        res = 0
        
        for i in range(1,len(keys)):
            if keys[i]-1==keys[i-1]:
                res = max(res,a[keys[i]]+a[keys[i-1]])
        
        return res
            