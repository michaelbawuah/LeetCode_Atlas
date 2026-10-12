#include <cstddef>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<long long> operands;
        for (const string& token : tokens) {
            const bool is_operator = token == "+" || token == "-" || token == "*" || token == "/";
            if (!is_operator) {
                std::size_t consumed = 0;
                const long long value = std::stoll(token, &consumed);
                if (consumed != token.size()) {
                    throw std::invalid_argument("invalid RPN operand");
                }
                check_range(value);
                operands.push_back(value);
                continue;
            }
            if (operands.size() < 2) {
                throw std::invalid_argument("RPN operator needs two operands");
            }
            const long long right = operands.back();
            operands.pop_back();
            const long long left = operands.back();
            operands.pop_back();
            long long value = 0;
            if (token == "+") {
                value = left + right;
            } else if (token == "-") {
                value = left - right;
            } else if (token == "*") {
                value = left * right;
            } else {
                if (right == 0) {
                    throw std::invalid_argument("RPN division by zero");
                }
                // Integer division truncates toward zero, including negative quotients.
                value = left / right;
            }
            check_range(value);
            operands.push_back(value);
        }
        if (operands.size() != 1) {
            throw std::invalid_argument("RPN expression must produce one result");
        }
        return static_cast<int>(operands.back());
    }

private:
    static void check_range(long long value) {
        if (value < std::numeric_limits<int>::min() || value > std::numeric_limits<int>::max()) {
            throw std::out_of_range("RPN intermediate result does not fit int");
        }
    }
};
