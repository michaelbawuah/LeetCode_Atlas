#pragma once

#include <cstddef>
#include <cstdint>
#include <limits>
#include <memory>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

#include <nlohmann/json.hpp>

using json = nlohmann::json;

struct ListNode {
    int val = 0;
    ListNode* next = nullptr;

    ListNode() = default;
    explicit ListNode(int value) : val(value) {}
};

class ListArena {
public:
    ListNode* build(const json& values) {
        if (!values.is_array()) {
            throw std::invalid_argument("a linked list must be a JSON integer array");
        }
        std::vector<std::unique_ptr<ListNode>> new_nodes;
        new_nodes.reserve(values.size());
        for (const json& value : values) {
            new_nodes.push_back(std::make_unique<ListNode>(read_value(value)));
        }
        for (std::size_t index = 1; index < new_nodes.size(); ++index) {
            new_nodes[index - 1]->next = new_nodes[index].get();
        }
        ListNode* head = new_nodes.empty() ? nullptr : new_nodes.front().get();
        // Moving unique_ptrs keeps node addresses stable and leaves older lists alive.
        nodes_.reserve(nodes_.size() + new_nodes.size());
        for (auto& node : new_nodes) {
            nodes_.push_back(std::move(node));
        }
        return head;
    }

private:
    static int read_value(const json& value) {
        if (!value.is_number_integer()) {
            throw std::invalid_argument("linked-list values must be integers");
        }
        if (value.is_number_unsigned()) {
            const auto number = value.get<std::uint64_t>();
            if (number > static_cast<std::uint64_t>(std::numeric_limits<int>::max())) {
                throw std::out_of_range("linked-list value does not fit int");
            }
            return static_cast<int>(number);
        }
        const auto number = value.get<std::int64_t>();
        if (number < std::numeric_limits<int>::min() || number > std::numeric_limits<int>::max()) {
            throw std::out_of_range("linked-list value does not fit int");
        }
        return static_cast<int>(number);
    }

    std::vector<std::unique_ptr<ListNode>> nodes_;
};

inline json list_to_json(const ListNode* head) {
    json values = json::array();
    std::unordered_set<const ListNode*> visited;
    while (head != nullptr) {
        if (!visited.insert(head).second) {
            throw std::invalid_argument("cannot serialize a cyclic linked list");
        }
        values.push_back(head->val);
        head = head->next;
    }
    return values;
}

inline json parse_case_args(const std::string& line) {
    json args = json::parse(line);
    if (!args.is_array()) {
        throw std::invalid_argument("each case must be a JSON argument array");
    }
    return args;
}
