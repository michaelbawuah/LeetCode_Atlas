#include <cstddef>
#include <vector>
using std::vector;
class Solution {
  public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph) {
        vector<vector<int>> answers;
        vector<int> path{0};
        visit(0, graph, path, answers);
        return answers;
    }

  private:
    static void visit(int node, const vector<vector<int>> &graph, vector<int> &path,
                      vector<vector<int>> &answers) {
        if (static_cast<std::size_t>(node) + 1 == graph.size()) {
            answers.push_back(path);
            return;
        }
        for (int neighbor : graph[node]) {
            path.push_back(neighbor);
            visit(neighbor, graph, path, answers);
            path.pop_back();
        }
    }
};
