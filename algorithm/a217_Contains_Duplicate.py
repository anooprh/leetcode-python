import os


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = set()
        for num in nums:
            if num in t: return True
            t.add(num)
        return False

if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().containsDuplicate([1,2,3,4]) == False
    assert Solution().containsDuplicate([1,2,3,2]) == True
    print " ---> Success"
