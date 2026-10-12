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
    const int k = args.at(1).get<int>();
    auto expected = original;
    const std::size_t group = static_cast<std::size_t>(k);
    for (std::size_t begin = 0; begin + group <= expected.size(); begin += group) {
        std::reverse(expected.begin() + static_cast<std::ptrdiff_t>(begin),
            expected.begin() + static_cast<std::ptrdiff_t>(begin + group));
    }
    Solution solution;
    ListNode* result = solution.reverseKGroup(head, k);
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
