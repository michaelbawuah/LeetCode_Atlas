#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    ListArena arena;
    std::vector<ListNode*> heads;
    for (const auto& values : args.at(0)) { heads.push_back(arena.build(values)); }
    Solution solution;
    return list_to_json(solution.mergeKLists(heads));
}
