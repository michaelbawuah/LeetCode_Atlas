#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    auto matrix = args.at(0).get<std::vector<std::vector<int>>>();
    solution.rotate(matrix);
    return matrix;
}
