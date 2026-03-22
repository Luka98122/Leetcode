from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        n1 = 0
        n2 = 0
        
        while True:
            if n1<m and n2<n:
                if nums1[n1]<nums2[n2]:
                    nums3.append(nums1[n1])
                    n1+=1
                else:
                    nums3.append(nums2[n2])
                    n2+=1
            else:
                if n1<m:
                    nums3.append(nums1[n1])
                    n1+=1
                elif n2<n:
                    nums3.append(nums2[n2])
                    n2+=1
                else:
                    break
        
        for i in range(m+n):
            nums1[i] =  nums3[i]

c = Solution()
a = [1,2,3,0,0,0]
print(a)