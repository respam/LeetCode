# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        number = x
        stack = []
        while x > 0:
            st_inp = x % 10
            x = x / 10
            stack.append(st_inp)

        print("Initial Stack")
        print(stack)

        size = len(stack)
        while len(stack) != 0:
            
