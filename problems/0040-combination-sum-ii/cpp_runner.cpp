#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto value0 = args.at(0).get<std::vector<int>>();
    auto value1 = args.at(1).get<int>();
    Solution object;
    return object.combinationSum2(value0, value1);
}
