#include <cstddef>
#include <queue>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>
using std::string;
using std::vector;
class Solution {
  public:
    int minMutation(const string &startGene, const string &endGene, vector<string> &bank) {
        if (startGene == endGene)
            return 0;
        std::unordered_set<string> available(bank.begin(), bank.end());
        if (!available.contains(endGene))
            return -1;
        std::unordered_set<string> seen{startGene};
        std::queue<std::pair<string, int>> pending;
        pending.emplace(startGene, 0);
        while (!pending.empty()) {
            const auto [gene, steps] = pending.front();
            pending.pop();
            for (std::size_t index = 0; index < gene.size(); ++index)
                for (char letter : string("ACGT")) {
                    string next = gene;
                    next[index] = letter;
                    if (available.contains(next) && seen.insert(next).second) {
                        if (next == endGene)
                            return steps + 1;
                        pending.emplace(next, steps + 1);
                    }
                }
        }
        return -1;
    }
};
