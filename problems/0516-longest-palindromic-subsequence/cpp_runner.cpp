#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto text = args.at(0).get<std::string>();
    Solution solution;
    return solution.longestPalindromeSubseq(text);
}
