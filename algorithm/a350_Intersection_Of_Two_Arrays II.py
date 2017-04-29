import os


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d, ans = {}, []
        d1 = self.gen_dict(nums1)
        d2 = self.gen_dict(nums2)
        for k in set(d1.keys()).intersection(set(d2.keys())):
            d[k] = min(d1[k], d2[k])

        for k in d:
            ans += [k for _ in range(d[k])]
        return ans

    def gen_dict(self, nums):
        d = {}
        for num in nums:
            d[num] = d[num] + 1 if num in d else 1
        return d


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    print(" ---> Success")
