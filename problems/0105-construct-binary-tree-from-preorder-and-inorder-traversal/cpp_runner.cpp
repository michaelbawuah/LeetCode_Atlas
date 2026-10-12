#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto preorder = args.at(0).get<std::vector<int>>();
    auto inorder = args.at(1).get<std::vector<int>>();
    Solution solution;
    TreeResultOwner result(solution.buildTree(preorder, inorder));
    return tree_to_json(result.get());
}
