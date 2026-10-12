#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto word1 = args.at(0).get<std::string>();
    auto word2 = args.at(1).get<std::string>();
    Solution solution;
    return solution.minDistance(word1, word2);
}
