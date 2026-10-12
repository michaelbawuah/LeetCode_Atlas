#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    std::vector<std::vector<char>> board;
    for (const auto& row : args.at(0)) {
        std::vector<char> decoded;
        for (const auto& value : row) {
            const std::string cell = value.get<std::string>();
            if (cell.size() != 1) {
                throw std::invalid_argument("Sudoku cells must be single characters");
            }
            decoded.push_back(cell.front());
        }
        board.push_back(std::move(decoded));
    }
    return solution.isValidSudoku(board);
}
