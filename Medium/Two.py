# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverse(self, num: int) -> int:
        rev = 0
        while num > 0:
            inp = num % 10
            rev = (rev * 10) + inp
            num = num // 10

        return rev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        num1 = 0
        num2 = 0

        while l1 is not None :
            num1 = (num1 * 10) + l1.val
            l1 = l1.next

        while l2 is not None:
            num2 = (num2 * 10) + l2.val
            l2 = l2.next

        num1 = Solution.reverse(Solution, num1)
        num2 = Solution.reverse(Solution, num2)

        total = num1 + num2

        head = ListNode(total % 10, None)
        l3 = head
        total = total // 10

        while total > 0:
            num = total % 10
            l3.next = ListNode(num, None)
            l3 = l3.next
            total = total // 10

        while head is not None:
            print(head.val)
            head = head.next
        # return head


if __name__ == '__main__':
    l1 = ListNode(2, None)
    l1.next = ListNode(4, None)
    l1.next.next = ListNode(3, None)

    l2 = ListNode(5, None)
    l2.next = ListNode(6, None)
    l2.next.next = ListNode(4, None)

    Solution.addTwoNumbers(Solution, l1, l2)
