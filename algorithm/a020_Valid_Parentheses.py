import os


class Solution(object):
    def checkClose(self, c, stack, open, close):
        if c == close:
            if len(stack) <= 0 or stack.pop() != open:
                return False
        return True

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[': stack.append(c)
            if not self.checkClose(c, stack, '(', ')'): return False
            if not self.checkClose(c, stack, '{', '}'): return False
            if not self.checkClose(c, stack, '[', ']'): return False
        return len(stack) == 0


if __name__ == "__main__":
    print "Running", os.path.basename(__file__),
    assert Solution().isValid("(){}[]") == True
    assert Solution().isValid("(){[}]") == False
    print " ---> Success"
