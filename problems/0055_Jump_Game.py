from typing import List
class BF_Solution:
    def canJump(self, nums: List[int]) -> bool:
        hm = {}
        n = len(nums)
        for i in range(n):
            hm[i] = []
        for i in range(n):
            for j in range(1,nums[i]+1):
                if (i+j>=n): break
                hm[i+j].append(i)
        
        stack = []
        ind = n-1
        visited = set()
        while True:
            if ind in visited: 
                if len(stack)==0: break
                ind = stack.pop()
                continue
            if (ind==0): return True
            possible = hm[ind]
            visited.add(ind)
            for thing in possible:
                stack.append(thing)
            if len(stack)==0: break
            ind = stack.pop()
        return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==0: return False
        if len(nums)==1: return True
        n = len(nums)
        last_max_reach = nums[0]
        max_reach = nums[0]
        sid = 0
        while True:
            for i in range(sid,max_reach+1):
                if i>=n-1: return True
                max_reach = max(max_reach,i+nums[i])
            
            if max_reach>=n-1: return True
            if max_reach == last_max_reach:
                return False
            sid = last_max_reach
            last_max_reach = max_reach
        
 
 
c = Solution()
#        0,1,2,3,4,5,6,7,8,9,10,11 
n_173 = [5,9,3,2,1,0,2,3,3,1, 0, 0]
n_1 = [2,3,1,1,4]
print(c.canJump([3,2,1,0,4]))           
            