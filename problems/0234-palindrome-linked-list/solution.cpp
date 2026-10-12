// ListNode is supplied by the judge or local adapter.
class Solution {
    static ListNode* reverse(ListNode* head) {
        ListNode* previous = nullptr;
        while (head != nullptr) {
            ListNode* following = head->next;
            head->next = previous;
            previous = head;
            head = following;
        }
        return previous;
    }

public:
    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return true;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* second = reverse(slow->next);
        ListNode* first = head;
        bool palindrome = true;
        for (ListNode* current = second; current != nullptr; current = current->next) {
            if (first->val != current->val) {
                palindrome = false;
            }
            first = first->next;
        }
        slow->next = reverse(second);
        return palindrome;
    }
};
