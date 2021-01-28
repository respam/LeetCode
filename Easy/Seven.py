# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:

    def inverse(self, num: int) -> int:
        rev = 0
        while num > 0:
            inp = num % 10
            rev = (rev * 10) + inp
            num = num // 10

        if abs(rev) > (2 ** 31 - 1):
            return 0

        return rev

    def reverse(self, x: int) -> int:
        if x < 0:
            x = x * -1
            result = Solution.inverse(Solution, x)
            result = result * -1

        else:
            result = Solution.inverse(Solution, x)

        print(result)
        return result


if __name__ == '__main__':
    Solution.reverse(Solution, 123)
    Solution.reverse(Solution, -123)
    Solution.reverse(Solution, 120)
    Solution.reverse(Solution, 0)
    Solution.reverse(Solution, 1534236469)

