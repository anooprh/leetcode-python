import os


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = [-float("inf")] * 3
        for i in range(3):
            for num in nums:
                if num > t[i]:
                    to_b = False
                    for j in range(i):
                        if t[j] == num:
                            to_b = True
                            break
                    if not to_b:
                        t[i] = num

        return t[2] if t[2] != -float("inf") else t[0]


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().thirdMax([3, 2, 1]) == 1
    assert Solution().thirdMax([2, 1]) == 2
    assert Solution().thirdMax([2, 2, 3, 1]) == 1
    print(" ---> Success")
