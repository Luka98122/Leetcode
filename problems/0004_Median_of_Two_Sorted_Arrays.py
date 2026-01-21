class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        length = len(nums1)+len(nums2)
        if length%2==1:
            a_ind = 0
            b_ind = 0
            a_len = len(nums1)
            b_len = len(nums2)
            cnt = 0
            while True:
                if a_ind == a_len:
                    return nums2[b_ind+(length//2 - cnt)]
                if b_ind == b_len:
                    return nums1[a_ind+(length//2 - cnt)]
                
                if nums1[a_ind] < nums2[b_ind]:
                    a_ind+=1
                    if a_ind+b_ind >= length//2:
                        return nums1[a_ind]
                elif nums2[b_ind] < nums1[a_ind]:
                    b_ind+=1
                    if a_ind+b_ind >= length//2:
                        return nums2[b_ind]
                else:
                    a_ind+=1
                    if a_ind+b_ind >= length//2:
                        return nums1[a_ind]
                cnt+=1

c = Solution()
c.findMedianSortedArrays([1,3],[2,2])