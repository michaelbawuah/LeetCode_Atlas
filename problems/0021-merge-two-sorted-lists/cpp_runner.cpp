#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    ListArena arena;
    ListNode* first = arena.build(args.at(0));
    ListNode* second = arena.build(args.at(1));
    Solution solution;
    return list_to_json(solution.mergeTwoLists(first, second));
}
