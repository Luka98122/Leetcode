from typing import List
class Solution:
    
    mappings = {
        '2':"abc",
        '3':"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"prqs",
        '8':"tuv",
        '9':"wxyz"
    }

    def solve(self, st, digits):
        if len(digits)==0:
            return [st]
        res = []
        for char in self.mappings[digits[0]]:
            nres = (self.solve(st+char,digits[1:]))
            for item in nres:
                res.append(item)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        
        return self.solve("",digits)

c = Solution()
print(c.letterCombinations("234"))