import os
import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        m = re.match("[\+\-]?\d+", str.lstrip())
        if m is None: return 0
        n = int(m.group())
        return min(n, 2147483647) if n > 0 else max(n, -2147483648)


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().myAtoi('123') == 123
    assert Solution().myAtoi('-123') == -123
    print " ---> Success"
