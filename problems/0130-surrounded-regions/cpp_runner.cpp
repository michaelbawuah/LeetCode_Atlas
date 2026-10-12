#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    std::vector<std::vector<char>> board;
    for (const auto& row : args.at(0)) {
        std::vector<char> decoded;
        decoded.reserve(row.size());
        for (const auto& cell : row) {
            const auto value = cell.get<std::string>();
            if (value.size() != 1) {
                throw std::invalid_argument("board cells must be one-character strings");
            }
            decoded.push_back(value.front());
        }
        board.push_back(std::move(decoded));
    }
    Solution solution;
    solution.solve(board);
    json result = json::array();
    for (const auto& row : board) {
        json encoded = json::array();
        for (const char cell : row) {
            encoded.push_back(std::string(1, cell));
        }
        result.push_back(std::move(encoded));
    }
    return result;
}
