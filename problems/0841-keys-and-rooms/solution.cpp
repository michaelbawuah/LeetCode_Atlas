#include <cstddef>
#include <vector>
using std::vector;
class Solution {
  public:
    bool canVisitAllRooms(vector<vector<int>> &rooms) {
        vector<unsigned char> seen(rooms.size(), 0);
        seen[0] = 1;
        vector<int> pending{0};
        std::size_t reached = 1;
        while (!pending.empty()) {
            int node = pending.back();
            pending.pop_back();
            for (int neighbor : rooms[node])
                if (!seen[neighbor]) {
                    seen[neighbor] = 1;
                    ++reached;
                    pending.push_back(neighbor);
                }
        }
        return reached == rooms.size();
    }
};
