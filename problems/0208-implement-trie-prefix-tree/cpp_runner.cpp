#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "Trie" || arguments.size() != operations.size()) throw std::invalid_argument("invalid design payload");
    Trie object;
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "insert") {
            object.insert(values.at(0).get<std::string>());
            output.push_back(nullptr);
        }
        else if (operations[index] == "search") {
            output.push_back(object.search(values.at(0).get<std::string>()));
        }
        else if (operations[index] == "startsWith") {
            output.push_back(object.startsWith(values.at(0).get<std::string>()));
        }
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
