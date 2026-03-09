from typing import List

class Solution:
    def solve(self,candidates,idx,target,pickedSoFar,sumSoFar):
        if sumSoFar == target:
            return [pickedSoFar]
        if sumSoFar>target or idx>=len(candidates):
            return None
        res = []
        res1 = self.solve(candidates,idx,target,pickedSoFar+[candidates[idx]],sumSoFar+candidates[idx])
        if res1!=None:
            for r in res1:
                res.append(r)
        
        res2 = self.solve(candidates,idx+1,target,pickedSoFar,sumSoFar)
        if res2!=None:
            for r in res2:
                res.append(r)
        
        return res


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        return self.solve(candidates,0,target,[],0)
    
c = Solution()
print(c.combinationSum([2,3,5],8))