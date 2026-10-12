#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto argument0 = args.at(0).get<std::string>();
    const auto argument1 = args.at(1).get<std::string>();
    Solution object;
    return object.addBinary(argument0, argument1);
}
