from typing import Optional


class Solution:
    def deleteDuplicates(self, head: "Optional[ListNode]") -> "Optional[ListNode]":
        dummy = ListNode(0, head)
        previous, current = dummy, head
        while current is not None:
            end = current
            while end.next is not None and end.next.val == current.val:
                end = end.next
            if end is current:
                previous = current
            else:
                previous.next = end.next
            current = end.next
        return dummy.next
