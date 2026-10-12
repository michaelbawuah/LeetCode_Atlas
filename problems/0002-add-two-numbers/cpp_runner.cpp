#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    ListArena arena;
    auto* first = arena.build(args.at(0));
    auto* second = arena.build(args.at(1));
    Solution solution;
    ListResultOwner result(solution.addTwoNumbers(first, second));
    return list_to_json(result.get());
}
