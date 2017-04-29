import os


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        childi = 0

        for si in s:
            if childi >= len(g): break
            if si >= g[childi]:
                childi += 1
        return childi


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().findContentChildren([1,2,3], [1,1]) == 1
    assert Solution().findContentChildren([1,2], [1,2,3]) == 2
    print(" ---> Success")
