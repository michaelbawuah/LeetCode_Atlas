#include <algorithm>
#include <tuple>

#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    ListArena arena;
    ListNode* head = arena.build(args.at(0));
    std::vector<std::tuple<ListNode*, int, ListNode*>> original;
    for (ListNode* node = head; node != nullptr; node = node->next) {
        original.emplace_back(node, node->val, node->next);
    }
    Solution solution;
    const bool result = solution.isPalindrome(head);
    for (const auto& [node, value, next] : original) {
        if (node->val != value || node->next != next) {
            throw std::logic_error("palindrome check did not restore original node links and values");
        }
    }
    return result;
}
