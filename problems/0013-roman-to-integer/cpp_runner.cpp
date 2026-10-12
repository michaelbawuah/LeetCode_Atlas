#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto argument0 = args.at(0).get<std::string>();
    Solution object;
    return object.romanToInt(argument0);
}
