#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "LRUCache" || arguments.size() != operations.size()) throw std::invalid_argument("invalid design payload");
    LRUCache object(arguments.at(0).at(0).get<int>());
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "get") {
            output.push_back(object.get(values.at(0).get<int>()));
        }
        else if (operations[index] == "put") {
            object.put(values.at(0).get<int>(), values.at(1).get<int>());
            output.push_back(nullptr);
        }
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
