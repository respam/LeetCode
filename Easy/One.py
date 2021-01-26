# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):

        checkTarget = {}

        count = 0
        for each in nums:
            if checkTarget.get(target - each) is None:
                checkTarget.update({each: count})
                count += 1

            else:
                print([checkTarget.get(target - each), count])
                return [checkTarget.get(target - each), count]


if __name__ == '__main__':
    Solution.twoSum(Solution, [2,7,11,15], 9)
    Solution.twoSum(Solution, [3,2,4], 6)
    Solution.twoSum(Solution, [3,3], 6)


# Faster Solution

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             try:
#                 return [i, nums[i+1:].index(target - nums[i])+i+1]
#             except:
#                 pass
