from typing import List
# 1min
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a = set()
        for candy in candyType:
            a.add(candy)
        
        return min(len(candyType)//2,len(a))