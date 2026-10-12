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
