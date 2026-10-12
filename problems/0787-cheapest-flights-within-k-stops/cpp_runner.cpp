#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto count = args.at(0).get<int>();
    auto flights = args.at(1).get<std::vector<std::vector<int>>>();
    auto src = args.at(2).get<int>();
    auto dst = args.at(3).get<int>();
    auto stops = args.at(4).get<int>();
    Solution solution;
    return solution.findCheapestPrice(count, flights, src, dst, stops);
}
