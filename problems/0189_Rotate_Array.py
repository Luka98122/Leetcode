from typing import List
class Solution:
    def easy(self, nums: List[int], k: int) -> None:
        if k == len(nums): return

        res = [0]*len(nums)

        for i in range(len(nums)):
            res[(i+k)%len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = res[i]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == len(nums): return

        n = len(nums)
        k = k % n

        def reverse(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)