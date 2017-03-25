import os


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows is 0: return []
        res = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(i-1):
                row.append(res[i-1][j]+res[i-1][j+1])
            row.append(1)
            res.append(row)
        return res

if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    print " ---> Success"
