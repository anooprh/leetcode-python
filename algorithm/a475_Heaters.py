import os
import bisect


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        ans = 0
        heaters.sort()
        for house in houses:
            l = bisect.bisect_left(heaters, house)
            ans = max(ans, min(abs(heaters[l - 1] - house) if l != 0 else float("inf"),
                               abs(heaters[l] - house) if l != len(heaters) else float("inf")))
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findRadius([1, 2, 3, 4], [1, 4]) == 1
    assert Solution().findRadius([1, 2, 3], [2]) == 1
    print(" ---> Success")
