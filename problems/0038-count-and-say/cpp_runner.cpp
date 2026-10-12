#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto value0 = args.at(0).get<int>();
    Solution object;
    return object.countAndSay(value0);
}
