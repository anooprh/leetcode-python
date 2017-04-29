import os


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        t1 = {}
        for num in nums:
            t1[num] = t1[num] + 1 if num in t1 else 1
        t2 = [(k,v) for (k,v) in zip(t1.keys(), t1.values())]
        t2.sort(key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(t2[i][0])
        return ans


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().topKFrequent([1,1,1,2,2,3], 2) == [1,2]
    print(" ---> Success")
