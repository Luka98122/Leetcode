from typing import List
class Solution:
    def linear(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if num not in hm: hm[num]=1
            else: hm[num]+=1
        
        for key in hm.keys():
            if hm[key]==1: return key
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num # XOR: a^a^b^b^c = c
        return res
