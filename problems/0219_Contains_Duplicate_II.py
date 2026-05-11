from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = set()
        
        for i in range(len(nums)):
            num = nums[i]
            if i-k-1>=0:
                a.remove(nums[i-k-1])
            
            if num in a:
                return True
            a.add(num)
        
        return False            