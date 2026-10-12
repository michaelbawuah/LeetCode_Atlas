#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto grid = args.at(0).get<std::vector<std::vector<int>>>();
    Solution solution;
    return solution.uniquePathsWithObstacles(grid);
}
