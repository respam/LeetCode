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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        rev1 = 0
        rev2 = 0
        rev_result = 0

        while l1 is not None:
            rev1 = (rev1 * 10) + l1.val
            rev2 = (rev2 * 10) + l2.val

            l1 = l1.next
            l2 = l2.next

        total = rev1 + rev2

        head = ListNode()
        head = ListNode(ListNode, total % 10)
        l3 = head
        total = total // 10

        while total > 0:
            num = total % 10
            l3.next = ListNode(ListNode, num)
            l3 = l3.next
            total = total // 10

        while head is not None:
            print(head.val)
            head = head.next
        # return head


if __name__ == '__main__':
    l1 = ListNode(ListNode, 2)
    l1.next = ListNode(ListNode, 4)
    l1.next.next = ListNode(ListNode, 3)

    l2 = ListNode(ListNode, 5)
    l2.next = ListNode(ListNode, 6)
    l2.next.next = ListNode(ListNode, 4)

    Solution.addTwoNumbers(Solution, l1, l2)
