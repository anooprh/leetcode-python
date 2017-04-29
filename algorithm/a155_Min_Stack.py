import os


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min = self.getMin()
        if min == None or x < min:
            min = x
        self.st.append((x, min))

    def pop(self):
        """
        :rtype: void
        """
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.st) == 0:
            return None
        else:
            return self.st[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.st) == 0:
            return None
        else:
            return self.st[-1][1]


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
    print(" ---> Success")
