import os


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        a_d, b_d, ab_d = {}, {}, {}
        for a in A:
            a_d[a] = a_d[a] + 1 if a in a_d else 1
        for b in B:
            b_d[b] = b_d[b] + 1 if b in b_d else 1
        for a in a_d:
            for b in b_d:
                ab_d[a + b] = ab_d[a + b] + (a_d[a] * b_d[b]) if (a + b) in ab_d else (a_d[a] * b_d[b])

        ans = 0
        for c in C:
            for d in D:
                k = -(c + d)
                if k in ab_d:
                    ans += ab_d[k]

        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().fourSumCount(A=[1, 2],
                                   B=[-2, -1],
                                   C=[-1, 2],
                                   D=[0, 2]) == 2
    print(" ---> Success")
