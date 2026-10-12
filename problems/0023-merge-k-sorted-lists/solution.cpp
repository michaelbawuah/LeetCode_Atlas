#include <queue>
#include <vector>

using std::vector;

// ListNode is supplied by the judge or local adapter.
class Solution {
    struct Later {
        bool operator()(const ListNode* first, const ListNode* second) const {
            return first->val > second->val;
        }
    };
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        std::priority_queue<ListNode*, vector<ListNode*>, Later> pending;
        for (ListNode* head : lists) { if (head != nullptr) { pending.push(head); } }
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (!pending.empty()) {
            ListNode* node = pending.top();
            pending.pop();
            ListNode* following = node->next;
            tail->next = node;
            tail = node;
            if (following != nullptr) { pending.push(following); }
        }
        tail->next = nullptr;
        return dummy.next;
    }
};
