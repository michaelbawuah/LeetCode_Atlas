#include <cstddef>
#include <cstdlib>
#include <exception>
#include <iostream>
#include <string>

#include "atlas_adapter.hpp"

json run_case(const json& args);

int main() {
    std::string line;
    std::size_t line_number = 0;
    while (std::getline(std::cin, line)) {
        ++line_number;
        try {
            const json result = run_case(parse_case_args(line));
            std::cout << result.dump() << '\n';
        } catch (const std::exception& error) {
            std::cerr << "case " << line_number << ": " << error.what() << '\n';
            return EXIT_FAILURE;
        }
    }
    if (std::cin.bad()) {
        std::cerr << "failed to read standard input\n";
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
