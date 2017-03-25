import os

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        sieve = [True] * n
        sieve[0] = False
        sieve[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                sieve[i * i:n:i] = [False] * len(sieve[i * i:n:i])

        return sum(sieve)


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().countPrimes(5) == 2
    assert Solution().countPrimes(25) == 9
    print " ---> Success"
