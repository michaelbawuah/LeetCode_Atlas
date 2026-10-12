#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto arg0 = args.at(0).get<double>();
    auto arg1 = args.at(1).get<int>();
    Solution solution;
    return solution.myPow(arg0, arg1);
}
