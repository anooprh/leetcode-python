import os


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for p1 in points:
            t = {}
            for p2 in points:
                d = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
                if d in t:t[d] += 1
                else: t[d] = 1
            for k in t:
                ans += t[k]*(t[k]-1)
        return ans

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]) == 2
    print(" ---> Success")
