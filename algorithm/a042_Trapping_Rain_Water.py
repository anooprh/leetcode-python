import os


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2: return 0
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])
        ans = 0
        for i, h in enumerate(height):
            ans += max(min(left[i], right[i]) - h, 0)
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    print(" ---> Success")
