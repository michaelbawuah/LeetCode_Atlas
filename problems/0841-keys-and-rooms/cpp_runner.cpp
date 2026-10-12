#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json &args) {
    auto rooms = args.at(0).get<vector<vector<int>>>();
    Solution solution;
    return solution.canVisitAllRooms(rooms);
}
