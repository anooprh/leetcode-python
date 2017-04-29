import math
import os


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        s = int(math.ceil(area ** 0.5))
        while (s <= area):
            o = area // s
            if (s * o == area): return [s, o]
            s += 1


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().constructRectangle(4) == [2,2]
    print(" ---> Success")
