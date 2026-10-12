#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "MyQueue" || operations.size() != arguments.size()) {
        throw std::invalid_argument("invalid design payload");
    }
    MyQueue object;
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "push") {
            object.push(values.at(0).get<int>());
            output.push_back(nullptr);
        }
        else if (operations[index] == "pop") {
            output.push_back(object.pop());
        }
        else if (operations[index] == "peek") {
            output.push_back(object.peek());
        }
        else if (operations[index] == "empty") {
            output.push_back(object.empty());
        }
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
