#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "MedianFinder" || operations.size() != arguments.size()) {
        throw std::invalid_argument("invalid design payload");
    }
    MedianFinder object;
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "addNum") {
            object.addNum(values.at(0).get<int>());
            output.push_back(nullptr);
        }
        else if (operations[index] == "findMedian") {
            output.push_back(object.findMedian());
        }
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
