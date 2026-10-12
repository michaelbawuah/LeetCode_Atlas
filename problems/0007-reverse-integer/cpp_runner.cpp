#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto argument0 = args.at(0).get<int>();
    Solution object;
    return object.reverse(argument0);
}
