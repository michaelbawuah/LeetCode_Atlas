#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "MinStack" || arguments.size() != operations.size()) throw std::invalid_argument("invalid design payload");
    MinStack object;
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "push") {
            object.push(values.at(0).get<int>());
            output.push_back(nullptr);
        }
        else if (operations[index] == "pop") {
            object.pop();
            output.push_back(nullptr);
        }
        else if (operations[index] == "top") {
            output.push_back(object.top());
        }
        else if (operations[index] == "getMin") {
            output.push_back(object.getMin());
        }
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
