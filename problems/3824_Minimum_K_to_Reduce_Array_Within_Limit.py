from typing import List
class Solution:
    def isValid(self,nums, k):
        if k==0: return False
        res = 0
        for num in nums:
            res+=num//k
            if num%k!=0: res+=1
        return res<=k*k
    def minimumK(self, nums: List[int]) -> int:
        l = 0
        r = 10**5
        lowest = 10**6 + 67
        while l<r:
            m = (l+r)//2
            if m==lowest:
                return lowest
            if self.isValid(nums,m):
                r = m
                lowest = min(m,lowest)
            else:
                l = m+1
        return lowest
c = Solution()
print(c.minimumK([1,3,3]))