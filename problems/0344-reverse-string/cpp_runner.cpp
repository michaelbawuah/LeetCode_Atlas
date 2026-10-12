#include "atlas_adapter.hpp"
#include "solution.cpp"
json run_case(const json& args) {
    std::vector<char> letters;
    for (const auto& item : args.at(0)) {
        const auto value = item.get<std::string>();
        if (value.size() != 1) throw std::invalid_argument("characters must be one-byte strings");
        letters.push_back(value.front());
    }
    Solution object; object.reverseString(letters); json output = json::array();
    for (char letter : letters) output.push_back(std::string(1,letter));
    return output;
}
