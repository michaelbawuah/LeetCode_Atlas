from typing import Optional


class Solution:
    def reverseKGroup(self, head: "Optional[ListNode]", k: int) -> "Optional[ListNode]":
        dummy = ListNode(0, head)
        group_previous = dummy
        while True:
            kth = group_previous
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            group_next = kth.next
            previous, current = group_next, group_previous.next
            while current is not group_next:
                following = current.next
                current.next = previous
                previous, current = current, following
            old_first = group_previous.next
            group_previous.next = kth
            group_previous = old_first
