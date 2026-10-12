#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "MyCircularDeque" || operations.size() != arguments.size()) {
        throw std::invalid_argument("invalid design payload");
    }
    auto initial0 = arguments.at(0).at(0).get<int>();
    MyCircularDeque object(initial0);
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "insertFront") {
            output.push_back(object.insertFront(values.at(0).get<int>()));
        }
        else if (operations[index] == "insertLast") {
            output.push_back(object.insertLast(values.at(0).get<int>()));
        }
        else if (operations[index] == "deleteFront") {
            output.push_back(object.deleteFront());
        }
        else if (operations[index] == "deleteLast") {
            output.push_back(object.deleteLast());
        }
        else if (operations[index] == "getFront") {
            output.push_back(object.getFront());
        }
        else if (operations[index] == "getRear") {
            output.push_back(object.getRear());
        }
        else if (operations[index] == "isEmpty") {
            output.push_back(object.isEmpty());
        }
        else if (operations[index] == "isFull") {
            output.push_back(object.isFull());
        }
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
