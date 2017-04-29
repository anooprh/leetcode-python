import os


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j=0,len(height)-1
        ans = 0
        while i<j:
            h = min(height[i], height[j])
            ans = max(ans, h*(j-i))
            while(height[j] <= h and i<j):j-=1
            while(height[i] <= h and i<j):i+=1
        return ans

if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().maxArea([1,2,3,3,2,1]) == 6
    print(" ---> Success")
