#include <cstddef>

// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy;
        dummy.next = head;
        ListNode* previous_group = &dummy;
        while (true) {
            ListNode* last = previous_group;
            for (int offset = 0; offset < k; ++offset) {
                last = last->next;
                if (last == nullptr) {
                    return dummy.next;
                }
            }
            ListNode* next_group = last->next;
            ListNode* previous = next_group;
            ListNode* current = previous_group->next;
            while (current != next_group) {
                ListNode* following = current->next;
                current->next = previous;
                previous = current;
                current = following;
            }
            ListNode* old_first = previous_group->next;
            previous_group->next = last;
            previous_group = old_first;
        }
    }
};
