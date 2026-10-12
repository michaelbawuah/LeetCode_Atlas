#pragma once

#include <cstddef>
#include <cstdint>
#include <limits>
#include <memory>
#include <optional>
#include <queue>
#include <stdexcept>
#include <string>
#include <unordered_map>
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

    ListNode* build_cycle(const json& payload) {
        if (!payload.is_object() || payload.size() != 2 || !payload.contains("values") ||
            !payload.contains("pos")) {
            throw std::invalid_argument("a cyclic list requires values and pos only");
        }
        const json& values = payload.at("values");
        const json& position = payload.at("pos");
        if (!values.is_array() || !position.is_number_integer()) {
            throw std::invalid_argument("cyclic-list values must be an array and pos an integer");
        }
        std::optional<std::size_t> cycle_index;
        if (position.is_number_unsigned()) {
            const auto index = position.get<std::uint64_t>();
            if (index >= values.size()) {
                throw std::invalid_argument("cyclic-list pos must be -1 or a valid node index");
            }
            cycle_index = static_cast<std::size_t>(index);
        } else {
            const auto index = position.get<std::int64_t>();
            if (index < -1 || (index >= 0 && static_cast<std::uint64_t>(index) >= values.size())) {
                throw std::invalid_argument("cyclic-list pos must be -1 or a valid node index");
            }
            if (index >= 0) {
                cycle_index = static_cast<std::size_t>(index);
            }
        }
        ListNode* head = build(values);
        if (cycle_index.has_value()) {
            ListNode* target = head;
            ListNode* last = head;
            for (std::size_t index = 0; index < *cycle_index; ++index) {
                target = target->next;
            }
            while (last->next != nullptr) {
                last = last->next;
            }
            last->next = target;
        }
        // Arena ownership is independent of next links, including cycles and self-links.
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

// Use only for freshly allocated result lists, never borrowed ListArena nodes.
class ListResultOwner {
public:
    explicit ListResultOwner(ListNode* head) : head_(head) {}
    ListResultOwner(const ListResultOwner&) = delete;
    ListResultOwner& operator=(const ListResultOwner&) = delete;
    ListResultOwner(ListResultOwner&& other) noexcept : head_(std::exchange(other.head_, nullptr)) {}
    ListResultOwner& operator=(ListResultOwner&&) = delete;

    ~ListResultOwner() {
        std::unordered_set<ListNode*> owned;
        ListNode* current = head_;
        while (current != nullptr && owned.insert(current).second) {
            current = current->next;
        }
        for (ListNode* node : owned) {
            delete node;
        }
    }

    ListNode* get() const noexcept {
        return head_;
    }

private:
    ListNode* head_;
};

struct TreeNode {
    int val = 0;
    TreeNode* left = nullptr;
    TreeNode* right = nullptr;

    TreeNode() = default;
    explicit TreeNode(int value) : val(value) {}
};

// Use only for freshly allocated result trees, never borrowed TreeArena nodes.
class TreeResultOwner {
public:
    explicit TreeResultOwner(TreeNode* root) : root_(root) {}
    TreeResultOwner(const TreeResultOwner&) = delete;
    TreeResultOwner& operator=(const TreeResultOwner&) = delete;
    TreeResultOwner(TreeResultOwner&& other) noexcept : root_(std::exchange(other.root_, nullptr)) {}
    TreeResultOwner& operator=(TreeResultOwner&&) = delete;

    ~TreeResultOwner() {
        std::vector<TreeNode*> pending;
        std::unordered_set<TreeNode*> owned;
        if (root_ != nullptr) {
            pending.push_back(root_);
        }
        while (!pending.empty()) {
            TreeNode* node = pending.back();
            pending.pop_back();
            if (node == nullptr || !owned.insert(node).second) {
                continue;
            }
            pending.push_back(node->left);
            pending.push_back(node->right);
        }
        for (TreeNode* node : owned) {
            delete node;
        }
    }

    TreeNode* get() const noexcept {
        return root_;
    }

private:
    TreeNode* root_;
};

class TreeArena {
public:
    TreeNode* build(const json& values) {
        if (!values.is_array()) {
            throw std::invalid_argument("a binary tree must be a JSON level-order array");
        }
        std::vector<std::optional<int>> decoded;
        decoded.reserve(values.size());
        for (const json& value : values) {
            decoded.push_back(value.is_null() ? std::nullopt : std::optional<int>(read_value(value)));
        }
        if (decoded.empty()) {
            return nullptr;
        }
        if (!decoded.front().has_value()) {
            for (const auto& value : decoded) {
                if (value.has_value()) {
                    throw std::invalid_argument("a null tree root cannot have descendants");
                }
            }
            return nullptr;
        }
        std::vector<std::unique_ptr<TreeNode>> new_nodes;
        new_nodes.push_back(std::make_unique<TreeNode>(*decoded.front()));
        TreeNode* root = new_nodes.front().get();
        std::queue<TreeNode*> parents;
        parents.push(root);
        std::size_t index = 1;
        while (!parents.empty() && index < decoded.size()) {
            TreeNode* parent = parents.front();
            parents.pop();
            for (int side = 0; side < 2 && index < decoded.size(); ++side, ++index) {
                if (!decoded[index].has_value()) {
                    continue;
                }
                new_nodes.push_back(std::make_unique<TreeNode>(*decoded[index]));
                TreeNode* child = new_nodes.back().get();
                if (side == 0) {
                    parent->left = child;
                } else {
                    parent->right = child;
                }
                parents.push(child);
            }
        }
        for (; index < decoded.size(); ++index) {
            if (decoded[index].has_value()) {
                throw std::invalid_argument("binary-tree array contains an unreachable node");
            }
        }
        nodes_.reserve(nodes_.size() + new_nodes.size());
        for (auto& node : new_nodes) {
            nodes_.push_back(std::move(node));
        }
        return root;
    }

private:
    static int read_value(const json& value) {
        if (!value.is_number_integer()) {
            throw std::invalid_argument("binary-tree values must be integers or null");
        }
        if (value.is_number_unsigned()) {
            const auto number = value.get<std::uint64_t>();
            if (number > static_cast<std::uint64_t>(std::numeric_limits<int>::max())) {
                throw std::out_of_range("binary-tree value does not fit int");
            }
            return static_cast<int>(number);
        }
        const auto number = value.get<std::int64_t>();
        if (number < std::numeric_limits<int>::min() || number > std::numeric_limits<int>::max()) {
            throw std::out_of_range("binary-tree value does not fit int");
        }
        return static_cast<int>(number);
    }

    std::vector<std::unique_ptr<TreeNode>> nodes_;
};

// Snapshot borrowed input identities for APIs that return an existing tree node.
class TreeReferences {
public:
    explicit TreeReferences(TreeNode* root) {
        std::vector<TreeNode*> pending;
        if (root != nullptr) {
            pending.push_back(root);
        }
        while (!pending.empty()) {
            TreeNode* node = pending.back();
            pending.pop_back();
            if (node == nullptr) {
                continue;
            }
            if (!original_.emplace(node, Snapshot{node->val, node->left, node->right}).second) {
                throw std::invalid_argument("tree references require an acyclic tree without shared children");
            }
            by_value_[node->val].push_back(node);
            pending.push_back(node->right);
            pending.push_back(node->left);
        }
    }

    TreeNode* resolve(int value) const {
        verify_unchanged();
        const auto found = by_value_.find(value);
        if (found == by_value_.end() || found->second.size() != 1) {
            throw std::invalid_argument("a tree reference must identify exactly one original node");
        }
        return found->second.front();
    }

    json serialize(TreeNode* node) const {
        verify_unchanged();
        if (node == nullptr) {
            return nullptr;
        }
        const auto found = original_.find(node);
        if (found == original_.end()) {
            throw std::invalid_argument("a tree-reference result must belong to the original tree");
        }
        return found->second.value;
    }

private:
    struct Snapshot {
        int value;
        TreeNode* left;
        TreeNode* right;
    };

    void verify_unchanged() const {
        for (const auto& [node, snapshot] : original_) {
            if (node->val != snapshot.value || node->left != snapshot.left || node->right != snapshot.right) {
                throw std::invalid_argument("tree-reference input labels and links must remain unchanged");
            }
        }
    }

    std::unordered_map<TreeNode*, Snapshot> original_;
    std::unordered_map<int, std::vector<TreeNode*>> by_value_;
};

inline json tree_to_json(const TreeNode* root) {
    json values = json::array();
    if (root == nullptr) {
        return values;
    }
    std::queue<const TreeNode*> nodes;
    std::unordered_set<const TreeNode*> visited;
    nodes.push(root);
    while (!nodes.empty()) {
        const TreeNode* node = nodes.front();
        nodes.pop();
        if (node == nullptr) {
            values.push_back(nullptr);
            continue;
        }
        if (!visited.insert(node).second) {
            throw std::invalid_argument("cannot serialize a cyclic or shared-node binary tree");
        }
        values.push_back(node->val);
        nodes.push(node->left);
        nodes.push(node->right);
    }
    while (!values.empty() && values.back().is_null()) {
        values.erase(values.size() - 1);
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
