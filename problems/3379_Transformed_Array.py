class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            val = nums[i]
            newPos = (i+val)%len(nums)
            res[i] = nums[newPos]
        return res
c = Solution()
print(c.constructTransformedArray([3,-2,1,1]))