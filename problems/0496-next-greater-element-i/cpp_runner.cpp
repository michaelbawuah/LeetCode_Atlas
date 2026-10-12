#include "atlas_adapter.hpp"
#include "solution.cpp"
json run_case(const json& args) {
    auto first=args.at(0).get<std::vector<int>>();auto second=args.at(1).get<std::vector<int>>();
    Solution object;return object.nextGreaterElement(first,second);
}
