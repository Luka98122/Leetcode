class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ind = 0
        n = len(nums)
        i = 0
        k = 0
        while i < n:
            if nums[i]!=val:
                nums[ind] = nums[i]
                ind+=1
                i+=1
                k+=1
            else:
                i+=1
        return k
        