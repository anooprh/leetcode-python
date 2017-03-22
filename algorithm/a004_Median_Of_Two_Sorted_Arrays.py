import os


class Solution(object):
    def __findKth(self, k, nums1, nums2, s1, s2):
        if s1 >= len(nums1):
            return nums2[s2 + k - 1]
        if s2 >= len(nums2):
            return nums1[s1 + k - 1]
        if k == 1:
            return min(nums1[s1], nums2[s2])

        m1 = s1 + k / 2 - 1
        m2 = s2 + k / 2 - 1

        mid1 = nums1[m1] if m1 < len(nums1) else float('inf')
        mid2 = nums2[m2] if m2 < len(nums2) else float('inf')

        if mid1 < mid2:
            return self.__findKth(k - k / 2, nums1, nums2, m1 + 1, s2)
        else:
            return self.__findKth(k - k / 2, nums1, nums2, s1, m2 + 1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        if total_len % 2 is 1:
            return self.__findKth(total_len / 2 + 1, nums1, nums2, 0, 0)
        else:
            return (self.__findKth(total_len / 2, nums1, nums2, 0, 0) + self.__findKth(total_len / 2 + 1, nums1, nums2, 0,
                                                                                       0)) / 2.0


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().findMedianSortedArrays([1, 3, 5, 7, 10], [2, 4, 6, 7]) == 5.0
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert Solution().findMedianSortedArrays([1], [2, 3]) == 2.0
    assert Solution().findMedianSortedArrays([2], []) == 2.0
    print " ---> Success"
