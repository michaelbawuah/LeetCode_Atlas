#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json &args) {
    vector<vector<char>> maze;
    for (const auto &row : args.at(0)) {
        vector<char> characters;
        for (const auto &cell : row) {
            characters.push_back(cell.get<std::string>().at(0));
        }
        maze.push_back(std::move(characters));
    }
    auto entrance = args.at(1).get<vector<int>>();
    Solution solution;
    return solution.nearestExit(maze, entrance);
}
