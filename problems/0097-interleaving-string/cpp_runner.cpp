#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto arg0 = args.at(0).get<std::string>();
    auto arg1 = args.at(1).get<std::string>();
    auto arg2 = args.at(2).get<std::string>();
    Solution solution;
    return solution.isInterleave(arg0, arg1, arg2);
}
