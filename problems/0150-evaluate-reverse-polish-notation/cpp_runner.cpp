#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto tokens = args.at(0).get<std::vector<std::string>>();
    Solution solution;
    return solution.evalRPN(tokens);
}
