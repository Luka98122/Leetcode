class Solution:
    def summaryRanges(self, nums):
        n = len(nums)
        p = 0
        ans = []
        while p < len(nums):
            s = p
            while p + 1 < n and nums[p + 1] == nums[p] + 1:
                p += 1
            if p == s:
                ans.append(str(nums[s]))
            else:
                ans.append(str(nums[s]) + "->" + str(nums[p]))
            p += 1
        return ans