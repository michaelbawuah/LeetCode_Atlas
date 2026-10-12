#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "MyCircularQueue" || operations.size() != arguments.size()) throw std::invalid_argument("invalid design payload");
    MyCircularQueue object(arguments.at(0).at(0).get<int>());
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "enQueue") output.push_back(object.enQueue(values.at(0).get<int>()));
        else if (operations[index] == "deQueue") output.push_back(object.deQueue());
        else if (operations[index] == "Front") output.push_back(object.Front());
        else if (operations[index] == "Rear") output.push_back(object.Rear());
        else if (operations[index] == "isEmpty") output.push_back(object.isEmpty());
        else if (operations[index] == "isFull") output.push_back(object.isFull());
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
