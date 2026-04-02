from typing import List
from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # TODO: Implement the actual binary search for O(n),
        # Don't use bisect_left (built-in python binary search)
        
        return bisect_left(nums,target)