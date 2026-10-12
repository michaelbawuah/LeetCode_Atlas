#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<double> calcEquation(std::vector<std::vector<std::string>>& equations,
                                      std::vector<double>& values,
                                      std::vector<std::vector<std::string>>& queries) {
        std::unordered_map<std::string, std::vector<std::pair<std::string, double>>> adjacent;
        for (std::size_t index = 0; index < equations.size(); ++index) {
            const auto& first = equations[index][0];
            const auto& last = equations[index][1];
            adjacent[first].emplace_back(last, values[index]);
            adjacent[last].emplace_back(first, 1.0 / values[index]);
        }
        std::vector<double> answers;
        answers.reserve(queries.size());
        for (const auto& query : queries) {
            if (!adjacent.contains(query[0]) || !adjacent.contains(query[1])) {
                answers.push_back(-1.0);
                continue;
            }
            std::unordered_set<std::string> seen{query[0]};
            std::vector<std::pair<std::string, double>> pending{{query[0], 1.0}};
            double answer = -1.0;
            while (!pending.empty()) {
                const auto [node, product] = pending.back();
                pending.pop_back();
                if (node == query[1]) {
                    answer = product;
                    break;
                }
                for (const auto& [neighbor, ratio] : adjacent.at(node)) {
                    if (seen.insert(neighbor).second) {
                        pending.emplace_back(neighbor, product * ratio);
                    }
                }
            }
            answers.push_back(answer);
        }
        return answers;
    }
};
