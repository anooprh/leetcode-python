import os


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return map(int, str(int(''.join(map(str, digits))) + 1))


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0]
    print " ---> Success"
