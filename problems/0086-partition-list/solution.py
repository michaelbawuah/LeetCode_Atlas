from typing import Optional


class Solution:
    def partition(self, head: "Optional[ListNode]", x: int) -> "Optional[ListNode]":
        smaller, larger = ListNode(0), ListNode(0)
        low, high = smaller, larger
        while head is not None:
            following = head.next
            head.next = None
            if head.val < x:
                low.next = head
                low = head
            else:
                high.next = head
                high = head
            head = following
        low.next = larger.next
        return smaller.next
