#include <algorithm>
#include <array>
#include <cstddef>
#include <utility>
#include <vector>

using std::vector;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        const int rows = static_cast<int>(grid.size());
        const int columns = static_cast<int>(grid[0].size());
        const std::array<std::pair<int, int>, 4> directions{{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}};
        int largest = 0;
        for (int row = 0; row < rows; ++row) {
            for (int column = 0; column < columns; ++column) {
                if (grid[row][column] != 1) {
                    continue;
                }
                grid[row][column] = 0;
                vector<std::pair<int, int>> pending{{row, column}};
                int area = 0;
                while (!pending.empty()) {
                    const auto [current_row, current_column] = pending.back();
                    pending.pop_back();
                    ++area;
                    for (const auto& [row_step, column_step] : directions) {
                        const int next_row = current_row + row_step;
                        const int next_column = current_column + column_step;
                        if (next_row >= 0 && next_row < rows && next_column >= 0 && next_column < columns &&
                            grid[next_row][next_column] == 1) {
                            grid[next_row][next_column] = 0;
                            pending.emplace_back(next_row, next_column);
                        }
                    }
                }
                largest = std::max(largest, area);
            }
        }
        return largest;
    }
};
