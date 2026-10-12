#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto begin = args.at(0).get<std::string>();
    auto end = args.at(1).get<std::string>();
    auto words = args.at(2).get<std::vector<std::string>>();
    Solution solution;
    return solution.ladderLength(begin, end, words);
}
