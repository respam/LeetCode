# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            print("False")
            return False

        reverse = 0
        number = x
        while x > 0:
            inp = x % 10
            reverse = (reverse * 10) + inp
            x = round(x / 10)
            print(x)

        print(reverse, number)
        if reverse == number:
            print("True")
            return True

        else:
            print("False")
            return False


if __name__ == '__main__':
    # Solution.isPalindrome(Solution, 121)
    # Solution.isPalindrome(Solution, -121)
    # Solution.isPalindrome(Solution, 31213)
    Solution.isPalindrome(Solution, 8)
