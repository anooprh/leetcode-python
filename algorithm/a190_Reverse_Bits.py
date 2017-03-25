import os


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{0:032b}'.format(n)[::-1], 2)


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().reverseBits(43261596) == 964176192
    print " ---> Success"
