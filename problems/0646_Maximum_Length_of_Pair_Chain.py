from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        if len(pairs) == 1: return 1
        if len(pairs) == 0: return 0
        n = len(pairs)

        cur = -2000
        ans = 0

        for i in range(0,n):
            if pairs[i][0] > cur:
                cur = pairs[i][1]
                ans+=1
        return ans
    
c = Solution()
print(c.findLongestChain([[1,2],[7,8],[4,5]]))