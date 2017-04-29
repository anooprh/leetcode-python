import os


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        while n > 0:
            if m == 0:
                for i in range(n): nums1[i] = nums2[i]
                break

            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    l1 = [1, 4, 7, None, None, None]
    Solution().merge(l1, 3, [2, 3, 6], 3)
    assert l1 == [1, 2, 3, 4, 6, 7]
    l1 = [1]
    Solution().merge(l1, 1, [], 0)
    assert l1 == [1]
    l1 = [1, 2, 4, 5, 6, 0]
    Solution().merge(l1, 5, [3], 1)
    assert l1 == [1, 2, 3, 4, 5, 6]
    l1 = [2, 0]
    Solution().merge(l1, 1, [1], 1)
    assert l1 == [1, 2]
    print(" ---> Success")
