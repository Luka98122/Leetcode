from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)
        def tree(nums,idx,sofar):
            if idx==n:
                if len(sofar)>1:
                    for j in range(1,len(sofar)):
                        if sofar[j-1]>sofar[j]: return
                    res.append(sofar)
                return
            
            tree(nums,idx+1,sofar+[nums[idx]])
            tree(nums,idx+1,sofar)
        
        tree(nums,0,[])

        se = set(tuple(x) for x in res)
        u_res = list(list(x) for x in se)

        return u_res

c = Solution()
print(c.findSubsequences([4,6,7,7]))