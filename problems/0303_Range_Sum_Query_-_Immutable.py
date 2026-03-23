class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        n = len(nums)
        pre=[0]
        s = 0
        for i in range(n):
            s+=nums[i]
            pre.append(s)
        self.pre = pre

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1]-self.pre[left]
