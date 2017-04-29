import os


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set([3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907,
                  43046721, 129140163, 387420489, 1162261467, 3486784401, 10460353203, 31381059609, 94143178827,
                  282429536481, 847288609443, 2541865828329, 7625597484987, 22876792454961, 68630377364883])
        return n in s


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().isPowerOfThree(3) == True
    assert Solution().isPowerOfThree(4) == False
    assert Solution().isPowerOfThree(9) == True
    assert Solution().isPowerOfThree(27) == True
    assert Solution().isPowerOfThree(81) == True
    print(" ---> Success")
