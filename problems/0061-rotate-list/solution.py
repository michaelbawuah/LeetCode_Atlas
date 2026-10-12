from typing import Optional


class Solution:
    def rotateRight(self, head: "Optional[ListNode]", k: int) -> "Optional[ListNode]":
        if head is None or head.next is None:
            return head
        tail, length = head, 1
        while tail.next is not None:
            tail = tail.next
            length += 1
        shift = k % length
        if shift == 0:
            return head
        new_tail = head
        for _ in range(length - shift - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        tail.next = head
        new_tail.next = None
        return new_head
