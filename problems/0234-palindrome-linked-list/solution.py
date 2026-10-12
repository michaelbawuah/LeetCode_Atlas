from typing import Optional


class Solution:
    def isPalindrome(self, head: "Optional[ListNode]") -> bool:
        if head is None or head.next is None:
            return True

        def reverse(start):
            previous = None
            while start is not None:
                following = start.next
                start.next = previous
                previous, start = start, following
            return previous

        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        second = reverse(slow.next)
        first, current = head, second
        palindrome = True
        while current is not None:
            if first.val != current.val:
                palindrome = False
            first, current = first.next, current.next
        slow.next = reverse(second)
        return palindrome
