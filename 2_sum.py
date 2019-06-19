class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        n = l1.val + l2.val
        l3 = ListNode(n % 10)
        l3.next = ListNode(n // 10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3, p3


solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l3, p3 = solution.addTwoNumbers(l1, l2)

