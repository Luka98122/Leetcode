class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = {}
        for i,n in enumerate(nums):
            if n not in a.keys():
                a[n] = []
            a[n].append(i)
        for i,n in enumerate(nums):
            if target-n in a.keys():
                if a[target-n][-1] != i:
                    return [a[n][0],a[target-n][-1]]
                