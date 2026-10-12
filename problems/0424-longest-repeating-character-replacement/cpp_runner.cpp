#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    return solution.characterReplacement(args.at(0).get<std::string>(), args.at(1).get<int>());
}
