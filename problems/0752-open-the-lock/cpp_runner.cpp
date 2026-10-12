#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json &args) {
    auto blocked = args.at(0).get<vector<string>>();
    auto target = args.at(1).get<string>();
    Solution solution;
    return solution.openLock(blocked, target);
}
