import os


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
    print(" ---> Success")
