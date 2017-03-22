import os
import re


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prev = "1"
        for i in range(n - 1):
            prev = self.genfrom(prev)
        return prev

    def genfrom(self, n):
        return "".join(
            [str(_[0]) + _[1] for _ in [(len(m.group(0)), m.group(1)) for m in re.finditer(r"(\d)\1*", n)]])


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
    print " ---> Success"
