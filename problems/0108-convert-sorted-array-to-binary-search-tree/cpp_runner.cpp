#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto values = args.at(0).get<std::vector<int>>();
    const auto original = values;
    Solution solution;
    TreeResultOwner result(solution.sortedArrayToBST(values));
    if (values != original) {
        throw std::logic_error("BST construction changed the sorted input array");
    }
    return tree_to_json(result.get());
}
