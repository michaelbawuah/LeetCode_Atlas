from heapq import heappop, heappush
from itertools import count
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: "List[Optional[ListNode]]") -> "Optional[ListNode]":
        serial = count()
        pending = []
        for head in lists:
            if head is not None:
                heappush(pending, (head.val, next(serial), head))
        dummy = ListNode(0)
        tail = dummy
        while pending:
            _, _, node = heappop(pending)
            following = node.next
            tail.next = node
            tail = node
            if following is not None:
                heappush(pending, (following.val, next(serial), following))
        tail.next = None
        return dummy.next
