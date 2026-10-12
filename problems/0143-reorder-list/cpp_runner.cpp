#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    ListArena arena;
    ListNode* head = arena.build(args.at(0));
    std::vector<std::pair<ListNode*, int>> original;
    for (ListNode* node = head; node != nullptr; node = node->next) {
        original.emplace_back(node, node->val);
    }
    std::vector<std::pair<ListNode*, int>> expected;
    for (std::size_t offset = 0; offset < original.size(); ++offset) {
        const std::size_t index = offset % 2 == 0 ? offset / 2 : original.size() - 1 - offset / 2;
        expected.push_back(original[index]);
    }
    Solution solution;
    solution.reorderList(head);
    ListNode* result = head;
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
    return list_to_json(head);
}
