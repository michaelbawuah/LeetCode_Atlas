#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::string simplifyPath(std::string path) {
        std::istringstream stream(path);
        std::vector<std::string> parts;
        std::string part;
        while (std::getline(stream, part, '/')) {
            if (part.empty() || part == ".") continue;
            if (part == "..") {
                if (!parts.empty()) parts.pop_back();
            } else parts.push_back(part);
        }
        std::string result;
        for (const auto& component : parts) { result += '/'; result += component; }
        return result.empty() ? "/" : result;
    }
};
