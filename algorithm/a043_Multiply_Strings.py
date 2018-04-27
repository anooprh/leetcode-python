import os


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        STEP = 3
        n1 = list(map(int, [num1[max(i - STEP, 0):i] for i in range(len(num1), 0, -STEP)]))
        n2 = list(map(int, [num2[max(i - STEP, 0):i] for i in range(len(num2), 0, -STEP)]))

        res = [0 for _ in range(len(n1) + len(n2) + 1)]
        for i, m1 in enumerate(n1):
            carry = 0
            for j, m2 in enumerate(n2):
                p = m1 * m2 + carry
                p1 = p % (10 ** STEP)
                c1 = p // (10 ** STEP)
                res[i + j] += p1
                carry = c1
            res[i + len(n2)] += carry
        rs = []
        c = 0
        for r in res:
            rs.append((r+c)%((10 ** STEP)))
            c = (r+c)//(10 ** STEP)
        rs.append(c)

        ans = ''.join(map(lambda x: "%03d" % (x), rs[::-1])).lstrip('0')
        return ans if ans != '' else '0'


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().multiply("123456789", "987654321") == "121932631112635269"
    print(" ---> Success")
