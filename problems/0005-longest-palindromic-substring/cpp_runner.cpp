#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto arg0 = args.at(0).get<std::string>();
    Solution solution;
    return solution.longestPalindrome(arg0);
}
