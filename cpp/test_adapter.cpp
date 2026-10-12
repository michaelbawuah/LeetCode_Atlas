#include <cstdint>
#include <limits>
#include <stdexcept>

#include <catch2/catch_test_macros.hpp>

#include "atlas_adapter.hpp"

TEST_CASE("Empty lists serialize as an empty JSON array") {
    ListArena arena;
    REQUIRE(arena.build(json::array()) == nullptr);
    REQUIRE(list_to_json(nullptr) == json::array());
}

TEST_CASE("List conversion preserves order and integer boundaries") {
    ListArena arena;
    const json values = json::array({std::numeric_limits<int>::min(), 0, std::numeric_limits<int>::max()});
    REQUIRE(list_to_json(arena.build(values)) == values);
    REQUIRE(list_to_json(arena.build(json::array({7}))) == json::array({7}));
}

TEST_CASE("One arena can own multiple independent lists") {
    ListArena arena;
    ListNode* first = arena.build(json::array({1, 2, 3}));
    ListNode* second = arena.build(json::array({4, 5}));
    REQUIRE(first != second);
    second->val = 9;
    REQUIRE(list_to_json(first) == json::array({1, 2, 3}));
    REQUIRE(list_to_json(second) == json::array({9, 5}));
}

TEST_CASE("Malformed lists leave previously built lists intact") {
    ListArena arena;
    ListNode* first = arena.build(json::array({1, 2}));
    REQUIRE_THROWS_AS(arena.build(json::object()), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({1, nullptr, 2})), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({1, 2.5})), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({true})), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({"3"})), std::invalid_argument);
    const auto above_max = static_cast<std::int64_t>(std::numeric_limits<int>::max()) + 1;
    const auto below_min = static_cast<std::int64_t>(std::numeric_limits<int>::min()) - 1;
    REQUIRE_THROWS_AS(arena.build(json::array({above_max})), std::out_of_range);
    REQUIRE_THROWS_AS(arena.build(json::array({below_min})), std::out_of_range);
    REQUIRE_THROWS_AS(arena.build(json::array({std::numeric_limits<std::uint64_t>::max()})), std::out_of_range);
    REQUIRE(list_to_json(first) == json::array({1, 2}));
    REQUIRE(list_to_json(arena.build(json::array({3, 4}))) == json::array({3, 4}));
}

TEST_CASE("Cyclic lists fail serialization instead of looping") {
    ListArena arena;
    ListNode* head = arena.build(json::array({1, 2, 3}));
    ListNode* last = head->next->next;
    last->next = head;
    REQUIRE_THROWS_AS(list_to_json(head), std::invalid_argument);
    last->next = nullptr;
    REQUIRE(list_to_json(head) == json::array({1, 2, 3}));
    ListNode* single = arena.build(json::array({9}));
    single->next = single;
    REQUIRE_THROWS_AS(list_to_json(single), std::invalid_argument);
    single->next = nullptr;
}

TEST_CASE("The line protocol accepts only one JSON argument array") {
    REQUIRE(parse_case_args("  [[1,2],3]  ") == json::array({json::array({1, 2}), 3}));
    REQUIRE(parse_case_args("[]") == json::array());
    REQUIRE_THROWS_AS(parse_case_args("{}"), std::invalid_argument);
    REQUIRE_THROWS_AS(parse_case_args("null"), std::invalid_argument);
    REQUIRE_THROWS_AS(parse_case_args("42"), std::invalid_argument);
    REQUIRE_THROWS_AS(parse_case_args(""), json::parse_error);
    REQUIRE_THROWS_AS(parse_case_args("[1,"), json::parse_error);
    REQUIRE_THROWS_AS(parse_case_args("[] []"), json::parse_error);
    REQUIRE(parse_case_args("[[9]]") == json::array({json::array({9})}));
}

TEST_CASE("Empty trees have a canonical empty-array serialization") {
    TreeArena arena;
    REQUIRE(arena.build(json::array()) == nullptr);
    REQUIRE(arena.build(json::array({nullptr})) == nullptr);
    REQUIRE(arena.build(json::array({nullptr, nullptr})) == nullptr);
    REQUIRE(tree_to_json(nullptr) == json::array());
}

TEST_CASE("Tree conversion preserves sparse level-order shapes and integer boundaries") {
    TreeArena arena;
    const json sparse = json::array({1, nullptr, 2, 3});
    REQUIRE(tree_to_json(arena.build(sparse)) == sparse);
    const json uneven = json::array({1, 2, 3, nullptr, 4, 5, nullptr, 6});
    REQUIRE(tree_to_json(arena.build(uneven)) == uneven);
    const json boundaries = json::array({0, std::numeric_limits<int>::min(), std::numeric_limits<int>::max()});
    REQUIRE(tree_to_json(arena.build(boundaries)) == boundaries);
    REQUIRE(tree_to_json(arena.build(json::array({8, nullptr, nullptr, nullptr}))) == json::array({8}));
}

TEST_CASE("Tree arenas keep earlier trees alive and isolate malformed input") {
    TreeArena arena;
    TreeNode* first = arena.build(json::array({4, 2, 6}));
    TreeNode* second = arena.build(json::array({7, nullptr, 9}));
    REQUIRE(first != second);
    second->right->val = 10;
    REQUIRE(tree_to_json(first) == json::array({4, 2, 6}));
    REQUIRE(tree_to_json(second) == json::array({7, nullptr, 10}));
    REQUIRE_THROWS_AS(arena.build(json::object()), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({nullptr, 1})), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({1, nullptr, nullptr, 2})), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({1, true})), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({1, 2.5})), std::invalid_argument);
    REQUIRE_THROWS_AS(arena.build(json::array({1, "2"})), std::invalid_argument);
    const auto above_max = static_cast<std::int64_t>(std::numeric_limits<int>::max()) + 1;
    const auto below_min = static_cast<std::int64_t>(std::numeric_limits<int>::min()) - 1;
    REQUIRE_THROWS_AS(arena.build(json::array({above_max})), std::out_of_range);
    REQUIRE_THROWS_AS(arena.build(json::array({below_min})), std::out_of_range);
    REQUIRE_THROWS_AS(arena.build(json::array({std::numeric_limits<std::uint64_t>::max()})), std::out_of_range);
    REQUIRE(tree_to_json(first) == json::array({4, 2, 6}));
    REQUIRE(tree_to_json(arena.build(json::array({11}))) == json::array({11}));
}

TEST_CASE("Tree serialization rejects cycles and repeated node identities") {
    TreeArena arena;
    TreeNode* root = arena.build(json::array({1, 2, 3}));
    TreeNode* left = root->left;
    left->left = root;
    REQUIRE_THROWS_AS(tree_to_json(root), std::invalid_argument);
    left->left = nullptr;
    TreeNode* right = root->right;
    root->right = left;
    REQUIRE_THROWS_AS(tree_to_json(root), std::invalid_argument);
    root->right = right;
    REQUIRE(tree_to_json(root) == json::array({1, 2, 3}));
}

TEST_CASE("New result trees stay alive through serialization and transfer ownership") {
    TreeArena borrowed;
    TreeNode* original = borrowed.build(json::array({4, 2, 6}));
    {
        auto* root = new TreeNode(4);
        root->left = new TreeNode(2);
        root->right = new TreeNode(6);
        TreeResultOwner first(root);
        TreeResultOwner moved(std::move(first));
        REQUIRE(first.get() == nullptr);
        REQUIRE(tree_to_json(moved.get()) == json::array({4, 2, 6}));
        REQUIRE(moved.get() != original);
    }
    REQUIRE(tree_to_json(original) == json::array({4, 2, 6}));
    TreeResultOwner empty(nullptr);
    REQUIRE(tree_to_json(empty.get()) == json::array());
}

TEST_CASE("Result ownership releases each node once even in malformed shared or cyclic trees") {
    auto* root = new TreeNode(1);
    auto* child = new TreeNode(2);
    root->left = child;
    root->right = child;
    child->left = root;
    TreeResultOwner owned(root);
    REQUIRE_THROWS_AS(tree_to_json(owned.get()), std::invalid_argument);
    // Sanitizer builds verify destruction avoids a leak, infinite loop, or double deletion.
}

TEST_CASE("New result lists preserve values and transfer ownership while borrowed lists live") {
    ListArena borrowed;
    ListNode* original = borrowed.build(json::array({7, 0, 8}));
    {
        auto* head = new ListNode(7);
        head->next = new ListNode(0);
        head->next->next = new ListNode(8);
        ListResultOwner first(head);
        ListResultOwner moved(std::move(first));
        REQUIRE(first.get() == nullptr);
        REQUIRE(moved.get() != original);
        REQUIRE(list_to_json(moved.get()) == json::array({7, 0, 8}));
    }
    REQUIRE(list_to_json(original) == json::array({7, 0, 8}));
    ListResultOwner empty(nullptr);
    REQUIRE(list_to_json(empty.get()) == json::array());
}

TEST_CASE("Fresh list ownership safely destroys cyclic results after serialization fails") {
    auto* head = new ListNode(1);
    auto* second = new ListNode(2);
    head->next = second;
    second->next = head;
    ListResultOwner owned(head);
    REQUIRE_THROWS_AS(list_to_json(owned.get()), std::invalid_argument);
    // Sanitizer builds verify every newly allocated node is deleted exactly once.
}
