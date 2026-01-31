class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        abc = "abcdefghijklmnopqrstuvwxyz"
        abc_hm = {
            
        }
        ind = 0
        for let in abc:
            abc_hm[let] = ind
            ind+=1
        for let in letters:
            if abc_hm[let]>abc_hm[target]:
                return let
        return letters[0]

c = Solution()
print(c.nextGreatestLetter(["c","f","j"],"z"))