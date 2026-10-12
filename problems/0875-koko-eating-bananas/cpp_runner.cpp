#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto piles = args.at(0).get<std::vector<int>>();
    const auto hours = args.at(1).get<int>();
    Solution solution;
    return solution.minEatingSpeed(piles, hours);
}
