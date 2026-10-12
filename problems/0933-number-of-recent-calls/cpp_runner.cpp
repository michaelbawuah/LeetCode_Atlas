#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    const auto operations = args.at(0).get<std::vector<std::string>>();
    const auto& arguments = args.at(1);
    if (operations.empty() || operations.front() != "RecentCounter" || operations.size() != arguments.size()) throw std::invalid_argument("invalid design payload");
    RecentCounter object;
    json output = json::array({nullptr});
    for (std::size_t index = 1; index < operations.size(); ++index) {
        const auto& values = arguments.at(index);
        static_cast<void>(values);
        if (operations[index] == "ping") output.push_back(object.ping(values.at(0).get<int>()));
        else throw std::invalid_argument("unknown design operation");
    }
    return output;
}
