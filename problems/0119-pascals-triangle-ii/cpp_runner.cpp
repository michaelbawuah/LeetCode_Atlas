#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    return solution.getRow(args.at(0).get<int>());
}
