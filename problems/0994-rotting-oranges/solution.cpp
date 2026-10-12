#include <array>
#include <cstddef>
#include <queue>
#include <utility>
#include <vector>

using std::vector;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if (grid.empty() || grid.front().empty()) {
            return 0;
        }
        const int rows = static_cast<int>(grid.size());
        const int columns = static_cast<int>(grid.front().size());
        std::queue<std::pair<int, int>> rotten;
        int fresh = 0;
        for (int row = 0; row < rows; ++row) {
            for (int column = 0; column < columns; ++column) {
                if (grid[row][column] == 2) {
                    rotten.emplace(row, column);
                } else if (grid[row][column] == 1) {
                    ++fresh;
                }
            }
        }
        const std::array<std::pair<int, int>, 4> directions{{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}};
        int minutes = 0;
        while (fresh > 0 && !rotten.empty()) {
            const std::size_t layer_size = rotten.size();
            for (std::size_t index = 0; index < layer_size; ++index) {
                const auto [row, column] = rotten.front();
                rotten.pop();
                for (const auto& [row_step, column_step] : directions) {
                    const int next_row = row + row_step;
                    const int next_column = column + column_step;
                    if (next_row >= 0 && next_row < rows && next_column >= 0 && next_column < columns &&
                        grid[next_row][next_column] == 1) {
                        grid[next_row][next_column] = 2;
                        --fresh;
                        rotten.emplace(next_row, next_column);
                    }
                }
            }
            ++minutes;
        }
        return fresh == 0 ? minutes : -1;
    }
};
