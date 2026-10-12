#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution object;
    return object.simplifyPath(args.at(0).get<std::string>());
}
