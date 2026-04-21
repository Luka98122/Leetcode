from typing import  List
class Solution: #A
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = {}
        stack = []


        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                mapping[smaller_num] = num
            
            stack.append(num)

        return [mapping.get(n, -1) for n in nums1]