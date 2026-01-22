class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        exp=-101
        nextInd = 0
        # This works because the judge only checks the first
        # k exepcted numbers and does not check if there is 
        # anything else in the array.
        while i < n:
            if nums[i]!=exp:
                exp = nums[i]
                nums[nextInd] = nums[i]
                nextInd+=1
            i+=1
        return nextInd

c = Solution()
print(c.removeDuplicates([1,1,2]))