#include <memory>
#include <vector>

// ListNode is supplied by the judge or local adapter.
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        int carry = 0;
        std::vector<std::unique_ptr<ListNode>> owned;
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int total = carry;
            if (l1 != nullptr) { total += l1->val; l1 = l1->next; }
            if (l2 != nullptr) { total += l2->val; l2 = l2->next; }
            carry = total / 10;
            owned.push_back(std::make_unique<ListNode>(total % 10));
            tail->next = owned.back().get();
            tail = tail->next;
        }
        for (auto& node : owned) { static_cast<void>(node.release()); }
        return dummy.next;
    }
};
