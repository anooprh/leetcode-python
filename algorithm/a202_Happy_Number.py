import os


class Solution(object):
    def isHappy(self, n, s=set()):
        """
        :type n: int
        :rtype: bool
        """
        val = sum(map(lambda x: int(x) * int(x), str(n)))
        if val == 1: return True
        if val in s: return False
        s.add(val)
        ans = self.isHappy(val, s)
        s.remove(val)
        return ans


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().isHappy(19) == True
    assert Solution().isHappy(13) == True
    assert Solution().isHappy(20) == False
    print " ---> Success"
