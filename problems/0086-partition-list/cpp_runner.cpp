#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    ListArena arena;
    auto* head = arena.build(args.at(0));
    const int x = args.at(1).get<int>();
    Solution solution;
    return list_to_json(solution.partition(head, x));
}
