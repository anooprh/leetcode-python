import os


class Solution(object):
    def fizzBuzz(self, n):
        return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    print("Running", os.path.basename(__file__), end=' ')
    assert Solution().fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    print(" ---> Success")
