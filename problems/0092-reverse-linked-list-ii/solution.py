from typing import Optional


class Solution:
    def reverseBetween(
        self, head: "Optional[ListNode]", left: int, right: int
    ) -> "Optional[ListNode]":
        dummy = ListNode(0, head)
        previous = dummy
        for _ in range(left - 1):
            previous = previous.next
        first = previous.next
        for _ in range(right - left):
            moved = first.next
            first.next = moved.next
            moved.next = previous.next
            previous.next = moved
        return dummy.next
