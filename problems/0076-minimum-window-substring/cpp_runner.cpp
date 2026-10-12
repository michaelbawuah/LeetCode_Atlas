#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto source = args.at(0).get<std::string>();
    const auto target = args.at(1).get<std::string>();
    Solution solution;
    return solution.minWindow(source, target);
}
