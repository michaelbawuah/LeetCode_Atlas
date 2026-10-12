#include "atlas_adapter.hpp"
#include "solution.cpp"

namespace {
int read_reference(const json& value) {
    if (!value.is_number_integer()) {
        throw std::invalid_argument("a tree reference must be an integer value");
    }
    if (value.is_number_unsigned()) {
        const auto decoded = value.get<std::uint64_t>();
        if (decoded > static_cast<std::uint64_t>(std::numeric_limits<int>::max())) {
            throw std::out_of_range("tree reference does not fit int");
        }
        return static_cast<int>(decoded);
    }
    const auto decoded = value.get<std::int64_t>();
    if (decoded < std::numeric_limits<int>::min() || decoded > std::numeric_limits<int>::max()) {
        throw std::out_of_range("tree reference does not fit int");
    }
    return static_cast<int>(decoded);
}
}

json run_case(const json& args) {
    TreeArena arena;
    TreeNode* root = arena.build(args.at(0));
    TreeReferences references(root);
    TreeNode* p = references.resolve(read_reference(args.at(1)));
    TreeNode* q = references.resolve(read_reference(args.at(2)));
    Solution solution;
    return references.serialize(solution.lowestCommonAncestor(root, p, q));
}
