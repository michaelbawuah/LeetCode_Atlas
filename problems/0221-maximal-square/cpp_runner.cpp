#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto encoded = args.at(0).get<std::vector<std::vector<std::string>>>();
    std::vector<std::vector<char>> matrix;
    for (const auto& row : encoded) {
        std::vector<char> characters;
        for (const auto& cell : row) {
            if (cell.size() != 1) {
                throw std::invalid_argument("matrix cells must be one character");
            }
            characters.push_back(cell.front());
        }
        matrix.push_back(std::move(characters));
    }
    Solution solution;
    return solution.maximalSquare(matrix);
}
