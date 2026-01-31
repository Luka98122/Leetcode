class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        s = 0
        end = len(letters)
        while s<end:
            mid = (s+end)//2
            if letters[mid]>target:
                end = mid
            else:
                s = mid+1
        if s>=len(letters):
            return letters[0]
        return letters[s]

c = Solution()
print(c.nextGreatestLetter(["c","f","j"],"z"))