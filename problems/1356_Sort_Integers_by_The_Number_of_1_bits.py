from typing import List
class Solution:
    def numBits(self, x : int) -> int:
        # Number of 1 bits
        res = 0
        while x>0:
            res+=x%2
            x//=2
        return res
            
            
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        # This feels like the naive approach
        new_arr = []
        for item in arr:
            new_arr.append([self.numBits(item),item])
        
        new_arr.sort()
        
        res = []
        for item in new_arr:
            res.append(item[1])
        return res