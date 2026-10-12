#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto value0 = args.at(0).get<std::string>();
    Solution object;
    return object.partition(value0);
}
