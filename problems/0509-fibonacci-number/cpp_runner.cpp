#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution object;
    return object.fib(args.at(0).get<int>());
}
