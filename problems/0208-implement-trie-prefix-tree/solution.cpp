#include <array>
#include <cstddef>
#include <string>
#include <vector>

class Trie {
    struct Node {
        std::array<int, 26> children;
        bool terminal = false;
        Node() { children.fill(-1); }
    };
    std::vector<Node> nodes_{1};
    int walk(const std::string& text) const {
        int node = 0;
        for (char letter : text) {
            node = nodes_[static_cast<std::size_t>(node)].children[static_cast<std::size_t>(letter - 'a')];
            if (node == -1) break;
        }
        return node;
    }
public:
    void insert(std::string word) {
        int node = 0;
        for (char letter : word) {
            const auto edge = static_cast<std::size_t>(letter - 'a');
            int following = nodes_[static_cast<std::size_t>(node)].children[edge];
            if (following == -1) {
                following = static_cast<int>(nodes_.size());
                nodes_[static_cast<std::size_t>(node)].children[edge] = following;
                nodes_.emplace_back();
            }
            node = following;
        }
        nodes_[static_cast<std::size_t>(node)].terminal = true;
    }
    bool search(std::string word) {
        const int node = walk(word);
        return node != -1 && nodes_[static_cast<std::size_t>(node)].terminal;
    }
    bool startsWith(std::string prefix) { return walk(prefix) != -1; }
};
