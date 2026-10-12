#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto text = args.at(0).get<std::string>();
    auto words = args.at(1).get<std::vector<std::string>>();
    Solution solution;
    return solution.wordBreak(text, words);
}
