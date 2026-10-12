#include <algorithm>
#include <tuple>

#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    ListArena arena;
    ListNode* head = arena.build(args.at(0));
    std::vector<std::pair<ListNode*, int>> original;
    for (ListNode* node = head; node != nullptr; node = node->next) {
        original.emplace_back(node, node->val);
    }
    const int left = args.at(1).get<int>();
    const int right = args.at(2).get<int>();
    auto expected = original;
    std::reverse(expected.begin() + left - 1, expected.begin() + right);
    Solution solution;
    ListNode* result = solution.reverseBetween(head, left, right);
    ListNode* current = result;
    for (const auto& [node, value] : expected) {
        if (current != node || current->val != value) {
            throw std::logic_error("list result changed original node identity, value, or ordering");
        }
        current = current->next;
    }
    if (current != nullptr) {
        throw std::logic_error("list result contains extra nodes or a cycle");
    }
    return list_to_json(result);
}
