# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        head.next = l1
        current = head.next
        past = head
        carry = 0
        while current and l2:
            current.val += l2.val + carry
            carry = current.val / 10
            current.val %= 10
            past = current
            current = current.next
            l2 = l2.next
        if l2:
            past.next = l2
        while carry != 0:
            if not past.next:
                past.next = ListNode(carry)
                break
            current = past.next
            current.val += carry
            carry = current.val / 10
            current.val %= 10
            past = current
        return head.next
l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)

Solution().addTwoNumbers(l1,l2)