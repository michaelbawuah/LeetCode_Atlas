#include <array>
#include <cstddef>
#include <memory>
#include <string>
#include <utility>
#include <vector>

class WordDictionary {
    struct Node {
        std::array<std::unique_ptr<Node>, 26> children{};
        bool terminal = false;
    };
    Node root_;

public:
    WordDictionary() = default;

    void addWord(std::string word) {
        Node* node = &root_;
        for (char letter : word) {
            auto& child = node->children[static_cast<std::size_t>(letter - 'a')];
            if (!child) child = std::make_unique<Node>();
            node = child.get();
        }
        node->terminal = true;
    }

    bool search(std::string word) {
        std::vector<const Node*> frontier{&root_};
        for (char letter : word) {
            std::vector<const Node*> following;
            for (const Node* node : frontier) {
                if (letter == '.') {
                    for (const auto& child : node->children) {
                        if (child) following.push_back(child.get());
                    }
                } else {
                    const auto& child = node->children[static_cast<std::size_t>(letter - 'a')];
                    if (child) following.push_back(child.get());
                }
            }
            if (following.empty()) return false;
            frontier = std::move(following);
        }
        for (const Node* node : frontier) {
            if (node->terminal) return true;
        }
        return false;
    }
};
