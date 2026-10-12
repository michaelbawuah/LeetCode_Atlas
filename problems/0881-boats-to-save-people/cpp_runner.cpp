#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    auto people = args.at(0).get<std::vector<int>>();
    return solution.numRescueBoats(people, args.at(1).get<int>());
}
