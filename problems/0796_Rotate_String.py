class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        #@Luka98122 - Ultra pythonic implementation (Never used this @ thing before, seemed interesting)
        # resStr = s+s
        # return len(s) == len(goal) and goal in resStr

        resStr = s+s
        for i in range(1,2*len(s)):
            if resStr[i:i+len(s)]==goal: return True
        
        return False